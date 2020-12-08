from ma import ma
from models.user import UserModel
# from schemas.report import ReportSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = UserModel

        load_only = ("password", )
        dump_only = ("id", )
        include_relationships = True
        load_instance = True
        exclude = ("admin", )
    # reports = ma.Nested(ReportSchema, many=True)
