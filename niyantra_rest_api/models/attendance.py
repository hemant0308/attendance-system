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


from .meta import Base

class AttendanceStatus(enum.Enum):
    PRESENT = 1
    OBSENT = 2
    LEAVE = 3

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    attendee_id = Column(Integer,ForeignKey('attendee.id'), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatus))
    created_at = Column(DateTime)
    attendee = relationship('Attendee')