from sqlalchemy import (
    Column,
    Index,
    Integer,
    Table,
    ForeignKey,
    String
)
from sqlalchemy.orm import relationship


from .trackable_base import Trackable
from .meta import Base


association_table = Table('user_role', Base.metadata,
    Column('user_id', Integer, ForeignKey('login_user.id')),
    Column('role_id', Integer, ForeignKey('role.id'))
)

class LoginUser(Trackable):
    __tablename__ = 'login_user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    fullname = Column(String)
    email = Column(String)
    roles = relationship("Role", secondary=association_table)


Index('login_user_idx_username', LoginUser.username, unique=True, mysql_length=25)
