from flask_restful import Resource
from flask import request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from models.user import UserModel
from schemas.user import UserSchema
from lib.util import max_err, max_res

USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."
USER_NO_PERMISSION = "No permission."

class User(Resource):
    @classmethod
    def get(cls, user_id: int):

        user = UserModel.find_by_id(user_id)
        user_schema = UserSchema()

        if not user:
            return max_err(USER_NOT_FOUND, 404)

        return max_res(user_schema.dump(user))

    @classmethod
    @jwt_required
    def delete(cls, user_id: int):

        if not user_id == get_jwt_identity():
            return max_err(USER_NO_PERMISSION, 400)

        user = UserModel.find_by_id(user_id)
        if not user:
            return max_err(USER_NOT_FOUND, 404)

        user.delete_from_db()
        return max_res(USER_DELETED)