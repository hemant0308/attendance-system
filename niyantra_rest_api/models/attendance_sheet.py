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

class AttendanceSheetStatus(enum.Enum):
    PENDING = 1
    SUBMITTED = 2
    DELETE = 3

class AttendanceSheet(Trackable):
    __tablename__ = 'attendance_sheet'
    id = Column(Integer, primary_key=True)
    section_session_id = Column(Integer, ForeignKey('section_session.id'), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceSheetStatus), default=AttendanceSheetStatus.PENDING)
    submitted_by = Column(Integer, ForeignKey('login_user.id'))
    submitted_on = Column(DateTime)
    section_session = relationship('SectionSession')
    attendances = relationship('Attendance', back_populates='attendance_sheet',lazy='select')