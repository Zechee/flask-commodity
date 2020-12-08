from ma import ma
from models.address import AddressModel


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AddressModel

        dump_only = ("id")
        include_relationships = True
        include_fk = True
        load_instance = True

