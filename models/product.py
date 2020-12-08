from db import db
from sqlalchemy import ForeignKey, func


class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    name = db.Column(db.String(80))
    photo = db.Column(db.String)
    intro = db.Column(db.Text)
    on_sale = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('CategoryModel', backref=db.backref('products', lazy=True))
    price = db.Column(db.Integer)
    market_price = db.Column(db.Integer)
    status = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())


    @classmethod
    def find_by_id(cls, _id: int) -> "ProductModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
