from pyramid.view import view_config, view_defaults

from niyantra_rest_api.models import LoginUser, Role
from niyantra_rest_api.schemas import UserSchema,LoginSchema
from niyantra_rest_api.services import UserService
from niyantra_rest_api.exceptions import ResourceNotFound, InvalidCredentials, CustomException
from niyantra_rest_api.utils import check_password, hash_password
from niyantra_rest_api.constants import Permissions

user_service = UserService()
user_schema = UserSchema()

@view_defaults(permission=Permissions.admin_only)
class UserController():
    def __init__(self, request):
        self.request = request
        user_service.set_request(request)

    @view_config(route_name='login',schema=LoginSchema, request_method='POST', permission=Permissions.every_one)
    def login_user(self):
        login_schema = self.request.validated
        user = user_service.get_user(login_schema['username'])
        if user is None:
            raise ResourceNotFound('username not found')
        is_valid = check_password(login_schema['password'], user.password)
        if not is_valid:
            raise InvalidCredentials
        roles = [str(role.name) for role in user.roles]
        token = self.request.create_jwt_token(user.id,roles=roles)
        return {'user':user_schema.dump(user),'token':token}

    @view_config(route_name='user', schema=UserSchema, response_schema=UserSchema, request_method='POST')
    def create_user(self):
        user_dict = self.request.validated
        return user_service.create_user(user_dict)

    @view_config(route_name='user_param', response_schema=UserSchema, request_method='GET')
    def get_user(self):
        user = user_service.get(int(self.request.matchdict['user_id']))
        if user is None:
            raise ResourceNotFound
        return user