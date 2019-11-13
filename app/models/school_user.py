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

class SchoolUser(Base):
    __tablename__ = 'school_user'
    id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('login_user.id'),nullable=False)
    school = relationship('School')
    user = relationship('LoginUser')
