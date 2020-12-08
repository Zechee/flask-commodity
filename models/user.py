from db import db
from lib.encrypt import encrypt_password, validate_password

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    username = db.Column(db.String(80), nullable=False, unique=True)
    email    = db.Column(db.String(80), unique=True)
    mobile   = db.Column(db.String(18), unique=True)
    password = db.Column(db.String(80))
    timezone = db.Column(db.String(16))
    admin    = db.Column(db.Boolean(), default=False)
    


    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    def set_password(self, password):
        self.password = encrypt_password(password)

    def check_password(self, password):
        return validate_password( self.password, password)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    def update(self) -> None:
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
