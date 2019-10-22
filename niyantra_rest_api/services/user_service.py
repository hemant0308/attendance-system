from sqlalchemy.orm.exc import NoResultFound

from niyantra_rest_api.services import BaseService
from niyantra_rest_api.models import LoginUser


class UserService(BaseService):
    def __init__(self):
        super(UserService, self).__init__(LoginUser)

    def get_user(request, username):
        try:
            return request.dbsession.query(LoginUser).filter(LoginUser.username == username).one()
        except NoResultFound:
            return None

