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

class Attendee(Base):
    __tablename__ = 'attendee'
    id = Column(Integer, primary_key=True)
    firstname = Column(String,nullable=False)
    lastname = Column(String)
