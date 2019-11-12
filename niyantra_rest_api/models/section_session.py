import enum

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Table,
    ForeignKey,
    String,
    Time,
    Enum
)
from sqlalchemy.orm import relationship


from .meta import Base

class WeekDay(enum.Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7

class SectionSession(Base):
    __tablename__ = 'section_session'
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('section.id'))
    start = Column(Time,nullable=False)
    end = Column(Time,nullable=False)
    day_of_week = Column(Enum(WeekDay), nullable=False)
    section = relationship('Section', back_populates='sessions')
