from ma import ma
from models.product import ProductModel


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel

        dump_only = ("id")
        include_relationships = True
        include_fk = True
        load_instance = True
