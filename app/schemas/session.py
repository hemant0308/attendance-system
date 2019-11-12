from datetime import datetime,date
from marshmallow import fields,Schema,post_load,validates_schema,ValidationError
from marshmallow_enum import EnumField

from app.models import (
    Attendance,
    AttendanceStatus,
    AttendanceSheet,
    Section,
    SectionSession,
    WeekDay
    )
from .trackable import TrackableSchema

class SectionSessionSchema(Schema):
    id = fields.Integer()
    start = fields.Time()
    end =fields.Time()
    day_of_week = EnumField(WeekDay, required=True)
    
    @validates_schema
    def validate_session(self, data, **kwargs):
        if data['start'] >= data['end']:
            raise ValidationError('start must be less than end')

    @post_load
    def get_obj(self, data, **kwargs):
        return SectionSession(**data)

class SectionSchema(Schema):
    id = fields.Integer()
    name =fields.String(required=True)
    @post_load
    def get_obj(self,data,**kwargs):
        return Section(**data)