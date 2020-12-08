from db import db
from sqlalchemy import ForeignKey, func


class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('orders', lazy=True))
    status = db.Column(db.String)
    address = db.Column(db.String)
    total_amount = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())


    @classmethod
    def find_by_id(cls, _id: int) -> "OrderModel":
        return cls.query.filter_by(id=_id).first()


    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    def update(self) -> None:
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

class OrderItemModel(db.Model):
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    order = db.relationship('OrderModel', backref=db.backref('order_items', lazy=True))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product = db.relationship('ProductModel', backref=db.backref('order_items', lazy=True))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer, default = 1)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @classmethod
    def find_by_id(cls, _id: int) -> "OrderItemModel":
        return cls.query.filter_by(id=_id).first()

    def update(self) -> None:
        db.session.commit()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
