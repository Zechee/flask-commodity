from ma import ma
from models.order import OrderModel, OrderItemModel


class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItemModel


        dump_only = ("id", "created_at")
        include_fk = True
        load_instance = True

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderModel

        dump_only = ("id" "created_at")
        include_relationships = True
        include_fk = True
        load_instance = True
    order_items = ma.Nested(OrderItemSchema, many=True)
    created_at = ma.Date()
    

