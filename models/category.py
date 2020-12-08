from db import db
from sqlalchemy import ForeignKey, func


class CategoryModel(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    parent_id = db.Column(db.Integer)
    depth = db.Column(db.Integer)
    order = db.Column(db.Integer)
    
    created_at = db.Column(db.DateTime, server_default=func.now())

    @classmethod
    def find_by_id(cls, _id: int) -> "CategoryModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
