from sqlalchemy.orm.exc import NoResultFound

from niyantra_rest_api.services import BaseService
from niyantra_rest_api.models import LoginUser, Role
from niyantra_rest_api.utils import hash_password
from niyantra_rest_api.exceptions import DuplicateEntry, CustomException

class UserService(BaseService):
    def __init__(self):
        super(UserService, self).__init__(LoginUser)

    def get_user(self, username):
        try:
            return self.dbsession.query(LoginUser).filter(LoginUser.username == username).one()
        except NoResultFound:
            return None

    def create_user(self, user_dict):
        user = self._get_user_object(user_dict)
        _user = self.get_user(user.username)
        if(_user is None):
            return self.create(user)
        else:
            raise DuplicateEntry("Username already existed")

    def _get_user_object(self, user_dict):
        roles = user_dict['roles']
        _roles = []
        for role in roles:
            roleObj = self.get_role(role)
            if roleObj is not None:
                _roles.append(roleObj)
            else:
                raise CustomException('Role with name : '+str(role)+' Not found')
        if len(_roles) == 0:
            raise CustomException('No roles found')
        del user_dict['roles']
        user = LoginUser(**user_dict)
        user.roles = _roles
        user.password = hash_password(user.password)
        return user

    def get_role(self, roleName):
        try:
            return self.dbsession.query(Role).filter(Role.name==roleName).one()
        except NoResultFound:
            return None