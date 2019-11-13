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

class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
