from pyramid.view import view_config

from niyantra_rest_api.models import LoginUser
from niyantra_rest_api.schemas import UserSchema,UserTokenSchema,LoginSchema
from niyantra_rest_api.services import user_service,encryption_service
from niyantra_rest_api.exceptions import UserNotFound,InvalidCredentials


@view_config(route_name='login',schema=LoginSchema, response_schema=UserTokenSchema, request_method="POST")
def login_user(request):
    login_schema = request.validated
    user = user_service.get_user(request,login_schema['username'])
    if user is None:
        raise UserNotFound
    is_valid = encryption_service.check_password(login_schema['password'], user['password'])
    if not is_valid:
        raise InvalidCredentials
    token = request.create_jwt_token(user.id)
    return UserTokenSchema.load({'user':user,token:token})
