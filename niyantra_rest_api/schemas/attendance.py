from datetime import datetime,date
from marshmallow import fields,Schema,post_load,validates_schema,ValidationError
from marshmallow_enum import EnumField

from niyantra_rest_api.models import (
    Attendance,
    AttendanceStatus,
    AttendanceSheetStatus,
    AttendanceSheet,
    Section,
    SectionSession
    )
from .student import StudentSchema
from .trackable import TrackableSchema
from .session import SectionSessionSchema

class AttendanceSchema(TrackableSchema):
    id = fields.Integer()
    attendance_sheet_id = fields.Integer(load_only=True)
    student = fields.Nested(StudentSchema,dump_only=True)
    student_id = fields.Integer(load_only=True,required=True)
    status = EnumField(AttendanceStatus)
    @post_load
    def get_obj(self,data,**kwargs):
        return Attendance(**data)
    def to_int(self,value,**kwargs):
        if isinstance(value,(datetime,date)):
            return value.timestamp()

class AttendanceSheetSchema(TrackableSchema):
    id = fields.Integer()
    date = fields.Date(required=True)
    session = fields.Nested(SectionSessionSchema,dump_only=True,attribute='section_session')
    status = EnumField(AttendanceSheetStatus, dump_only=True)
    session_id =fields.Integer(load_only=True,attribute='section_session_id', required=True)
    created_at = fields.DateTime(dump_only=True)
    created_by = fields.String(dump_only=True)

    @validates_schema
    def validate_date(self, data, **kwargs):
        if data['date'] > datetime.now().date():
            raise ValidationError('date must be less than or equals to current date','date')

    @post_load
    def get_obj(self, data, **kwargs):
        return AttendanceSheet(**data)
