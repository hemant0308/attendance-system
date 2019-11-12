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

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('login_user.id'), nullable=False)
    user = relationship('LoginUser')
    sectionSessions = relationship('TeacherSession')

Index('teacher_idx_user_id', Teacher.user_id, unique=True, mysql_length=25)
