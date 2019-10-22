from datetime import datetime,date
from marshmallow import fields,Schema,post_load
from marshmallow_enum import EnumField

from niyantra_rest_api.models import Attendance,AttendanceStatus
from niyantra_rest_api.schemas.attendee import AttendeeSchema

class AttendanceSchema(Schema):
    id = fields.String()
    attendee = fields.Nested(AttendeeSchema,dump_only=True)
    attendee_id = fields.Integer(load_only=True,required=True)
    date = fields.Date()
    status = EnumField(AttendanceStatus)
    created_at = fields.DateTime()
    @post_load
    def get_obj(self,data,**kwargs):
        return Attendance(**data)
    def to_int(self,value,**kwargs):
        if isinstance(value,(datetime,date)):
            return value.timestamp()