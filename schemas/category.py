from ma import ma
from models.category import CategoryModel


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel

        dump_only = ("id")
        include_relationships = True
        include_fk = True
        load_instance = True

