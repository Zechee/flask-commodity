from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from marshmallow import ValidationError

from config import app_config
from lib.util import max_err
from db import db
from ma import ma
from router import router


from seeds import init_database, add_address, add_category, add_order, add_orderitem, add_product
from blacklist import BLACKLIST
from resources.session import UserProfile, UserRegister, UserLogin, TokenRefresh, UserLogout, UserInfo


app = Flask(__name__)
app.config.from_object(app_config['development'])
db.init_app(app)
ma.init_app(app)
api = Api(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# @app.before_first_request
@app.cli.command("seed")
def seed():
    db.create_all()
    init_database(db)
   

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return max_err(err.messages, 400)


# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST


api.prefix = '/api'

api.add_resource(UserRegister, "/register")
# api.add_resource(User, "/user/<int:user_id>")  # for security concerns
api.add_resource(UserInfo, "/userinfo")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")
api.add_resource(UserProfile,"/profile")
router(api)

if __name__ == "__main__":
    app.run(port=5000, debug=True)