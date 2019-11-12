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

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer,ForeignKey('section.id'))
    firstname = Column(String,nullable=False)
    lastname = Column(String)
    section = relationship('Section')
