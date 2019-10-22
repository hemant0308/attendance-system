from marshmallow import ValidationError
from pyramid.view import exception_view_config

from niyantra_rest_api.exceptions import UserNotFound,InvalidCredentials,NoResourceFound,ConstraintError

@exception_view_config(ValidationError,renderer='json')
def validation_error_view(exception, request):
    request.response.status_code = 400
    return {
        "message": "Invalid request type",
        "errors": exception.messages
    }

@exception_view_config(UserNotFound, renderer='json')
def user_not_found_view(exception, request):
    request.response.status_code = 404
    return {
        "message": "Username not found"
    }

@exception_view_config(InvalidCredentials, renderer='json')
def invalid_credentials_view(exception, request):
    request.response.status_code = 401
    return {
        "message": "Invalid username or password"
    }

@exception_view_config(NoResourceFound, renderer='json')
def invalid_credentials_view(exception, request):
    request.response.status_code = 404
    return {
        "message": "No Resource Found"
    }

@exception_view_config(ConstraintError, renderer='json')
def constraint_error(exception, request):
    request.response.status_code = 400
    return {
        "message": str(exception)
    }