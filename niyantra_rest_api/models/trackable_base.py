import enum

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey
)

from sqlalchemy.ext.declarative import declared_attr

from .meta import Base


class Trackable(Base):
    __abstract__ = True
    created_at = Column(DateTime,nullable=False)
    @declared_attr
    def created_by(cls):
        return Column(Integer,ForeignKey('login_user.id'),nullable=False)
    updated_at = Column(DateTime, nullable=True)
    @declared_attr
    def updated_by(cls):
        return Column(Integer,ForeignKey('login_user.id'),nullable=True)
