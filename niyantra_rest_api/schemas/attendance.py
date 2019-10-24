from datetime import datetime,date
from marshmallow import fields,Schema,post_load,validates_schema,ValidationError
from marshmallow_enum import EnumField

from niyantra_rest_api.models import Attendance,AttendanceStatus,AttendanceSheet,Section, Section
from .student import StudentSchema
from .trackable import TrackableSchema

class AttendanceSchema(TrackableSchema):
    id = fields.Integer()
    attendance_sheet_id = fields.Integer()
    student = fields.Nested(StudentSchema,dump_only=True)
    student_id = fields.Integer(load_only=True,required=True)
    status = EnumField(AttendanceStatus)
    @post_load
    def get_obj(self,data,**kwargs):
        return Attendance(**data)
    def to_int(self,value,**kwargs):
        if isinstance(value,(datetime,date)):
            return value.timestamp()

class SectionSessionSchema(Schema):
    id = fields.Integer()
    section_id = fields.Integer(load_only=True)
    start = fields.Time()
    end =fields.Time()
    @validates_schema
    def validate_session(self, data, **kwargs):
        if data['start'] >= data['end']:
            raise ValidationError('start must be less than end')

    @post_load
    def get_obj(self, data, **kwargs):
        return Section(**data)

class SectionSchema(Schema):
    id = fields.Integer()
    name =fields.String()
    sessions = fields.Nested(SectionSessionSchema,many=True)
    @post_load
    def get_obj(self,data,**kwargs):
        return Section(**data)

class AttendanceSheetSchema(TrackableSchema):
    id = fields.Integer()
    date = fields.Date()
    session = fields.Nested(SectionSessionSchema,dump_only=True,attribute='section_session')
    section_session_id =fields.Integer(load_only=True)
    attendances = fields.Nested(AttendanceSchema, dump_only=True, many=True)
    created_at = fields.DateTime(dump_only=True)
    created_by = fields.String(dump_only=True)
    @post_load
    def get_obj(self, data, **kwargs):
        return AttendanceSheet(**data)
