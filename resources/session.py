from flask_restful import Resource
from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)
from models.user import UserModel

from schemas.user import UserSchema
from blacklist import BLACKLIST
from lib.util import max_res, max_err
USER_ALREADY_EXISTS = "A user with that username already exists."
CREATED_SUCCESSFULLY = "User <{username}> created successfully."
UPDATED_SUCCESSFULLY = "A User has updated successfully."
USER_NO_PASSWORD = "User need a password."
USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."
INVALID_CREDENTIALS = "Invalid credentials!"
USER_LOGGED_OUT = "User <id={user_id}> successfully logged out."
USER_NO_PERMISSION = "No permission."

class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = UserSchema().load(user_json)

        if not user.password:
            return max_err(USER_NO_PASSWORD, 404)

        if UserModel.find_by_username(user.username):
            return max_err(USER_ALREADY_EXISTS, 400)

        user.set_password(user.password)
        user.save_to_db()

        return max_res(CREATED_SUCCESSFULLY.format(username=user.username), 201)


class UserInfo(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)
        if not user:
            return max_err(USER_NOT_FOUND, 404)
        return max_res(UserSchema().dump(user))

class UserProfile(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        user_json = request.get_json()
        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)

        if 'password' in user_json.keys():
            user.set_password(user_json['password'])

        # update all fields from updatable_fields
        # original codes:
        # if 'fullname' in user_json.keys():
        #     user.fullname = user_json['fullname']

        updatable_fields = ['fullname', 'timezone', 'email', 'mobile']
        for f in updatable_fields:
            if f in user_json.keys():
                setattr(user, f, user_json[f])

        user.update()
        return max_res(UPDATED_SUCCESSFULLY)

class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = UserSchema().load(user_json)

        user = UserModel.find_by_username(user_data.username)

        if user and user.check_password(user_data.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return max_res({
                "token": access_token,
                "refresh_token": refresh_token
            })

        return max_err(INVALID_CREDENTIALS, 401)


class UserLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()[
            "jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        user_id = get_jwt_identity()

        BLACKLIST.add(jti)
        return max_res(USER_LOGGED_OUT.format(user_id=user_id))


class TokenRefresh(Resource):
    @classmethod
    @jwt_refresh_token_required
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return max_res({"access_token": new_token})
