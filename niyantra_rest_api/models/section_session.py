from sqlalchemy import (
    Column,
    Index,
    Integer,
    Table,
    ForeignKey,
    String,
    Time
)
from sqlalchemy.orm import relationship


from .meta import Base

class SectionSession(Base):
    __tablename__ = 'section_session'
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('section.id'))
    start = Column(Time,nullable=False)
    end = Column(Time,nullable=False)
    section = relationship('Section', back_populates='sessions')
