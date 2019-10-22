from sqlalchemy import (
    Column,
    Integer,
    String
)

from .meta import Base


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

