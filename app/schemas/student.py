from marshmallow import fields,Schema,post_load

from app.models import Student
from .session import SectionSchema

class StudentSchema(Schema):
    id = fields.String()
    section_id = fields.Int(required=True,load_only=True)
    firstname = fields.String(required=True)
    lastname = fields.String()
    @post_load
    def get_obj(self,data,**kwargs):
        return Student(**data)