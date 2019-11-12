
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Table,
    ForeignKey,
    String,
    Enum
)
from sqlalchemy.orm import relationship


from .meta import Base


class TeacherSession(Base):
    __tablename__ = 'teacher_session'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer,ForeignKey('teacher.id'))
    section_session_id = Column(Integer,ForeignKey('section_session.id'))
    teacher = relationship('Teacher')
    section_session = relationship('SectionSession')