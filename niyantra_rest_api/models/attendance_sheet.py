import enum

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Table,
    ForeignKey,
    String,
    DateTime,
    Enum,
    Date
)
from sqlalchemy.orm import relationship


from .trackable_base import Trackable

class AttendanceSheet(Trackable):
    __tablename__ = 'attendance_sheet'
    id = Column(Integer, primary_key=True)
    section_session_id = Column(Integer, ForeignKey('section_session.id'), nullable=False)
    date = Column(Date, nullable=False)
    section_session = relationship('SectionSession')
    attendances = relationship('Attendance', back_populates='attendance_sheet',lazy='select')