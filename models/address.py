from db import db
from sqlalchemy import ForeignKey, func


class AddressModel(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('addresses', lazy=True))
    name = db.Column(db.String(80))
    number = db.Column(db.String, nullable=False)
    address = db.Column(db.String(80), nullable=False)

    created_at = db.Column(db.DateTime, server_default=func.now())


    @classmethod
    def find_by_id(cls, _id: int) -> "AddressModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
