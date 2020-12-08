import os

config_path = os.path.abspath(os.path.dirname(__file__))


class Config:

    # SQLALCHEMY_DATABASE_URI = os.environ.get(
    #     "DATABASE_URL",
    #     'mysql://user:pwd@127.0.0.1:3306/dbname?charset=utf8')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True

    JWT_BLACKLIST_ENABLED = True  # enable blacklist feature
    JWT_BLACKLIST_TOKEN_CHECKS = [
        "access",
        "refresh",
    ]  # allow blacklisting for access and refresh tokens

    JWT_ACCESS_TOKEN_EXPIRES=86400
    
    BUNDLE_ERRORS = True
    SECRET_KEY = os.environ.get(
        'SECRET_KEY', '3j4k5h43kj5hj234b5jh34bk25b5k234j5bk2j3rref3b532')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}