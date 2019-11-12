from marshmallow import fields,Schema,post_load
from marshmallow_enum import EnumField

from app.models import Teacher, TeacherSession
from .user import UserSchema
from .session import SectionSchema,SectionSessionSchema

class TeacherSchema(Schema):
    id = fields.Int()
    user = fields.Nested(UserSchema, dump_only=True)
    username = fields.String(load_only=True, required=True)
    fullname = fields.String(load_only=True, required=True)

class TeacherSessionSchema(Schema):
    id = fields.Int()
    session_id = fields.Int(load_only=True, attribute='section_session_id', required=True)
    section = fields.Nested(SectionSchema,attribute='section_session.section', dump_only=True)
    session = fields.Nested(SectionSessionSchema, dump_only=True, attribute='section_session')
    @post_load
    def get_obj(self,data,**kwargs):
        return TeacherSession(**data)