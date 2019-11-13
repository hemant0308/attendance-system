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

class AttendanceStatus(enum.Enum):
    PRESENT = 1
    ABSENT = 2
    LEAVE = 3

class Attendance(Trackable):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer,ForeignKey('student.id'), nullable=False)
    attendance_sheet_id = Column(Integer,ForeignKey('attendance_sheet.id'), nullable=False)
    status = Column(Enum(AttendanceStatus))
    student = relationship('Student')
    attendance_sheet = relationship('AttendanceSheet', back_populates='attendances')

