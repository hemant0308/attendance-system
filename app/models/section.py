from sqlalchemy import (
    Column,
    Index,
    Integer,
    Table,
    ForeignKey,
    String
)
from sqlalchemy.orm import relationship


from .meta import Base

class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
    sessions = relationship('SectionSession', back_populates='section')
    school = relationship('School')
