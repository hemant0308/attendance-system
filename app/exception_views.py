import traceback

from marshmallow import ValidationError
from pyramid.view import exception_view_config
from pyramid.httpexceptions import HTTPForbidden

from app.exceptions import (
    ResourceNotFound,
    InvalidCredentials,
    ConstraintError,
    AttendanceSubmitted,
    DuplicateEntry,
    CustomException,
    UnAuthorized
    )

@exception_view_config(ValidationError,renderer='json')
def validation_error_view(exception, request):
    request.response.status_code = 400
    return {
        "message": "Invalid request type",
        "errors": exception.messages
    }

@exception_view_config(ResourceNotFound, renderer='json')
def resource_found_view(exception, request):
    request.response.status_code = 404
    return {
        "message": str(exception)
    }

@exception_view_config(InvalidCredentials, renderer='json')
def invalid_credentials_view(exception, request):
    request.response.status_code = 401
    return {
        "message": "Invalid username or password"
    }

@exception_view_config(ConstraintError, renderer='json')
@exception_view_config(CustomException, renderer='json')
def constraint_error(exception, request):
    request.response.status_code = 400
    return {
        "message": str(exception)
    }

@exception_view_config(AttendanceSubmitted, renderer='json')
@exception_view_config(DuplicateEntry, renderer='json')
def conflict_error(exception, request):
    request.response.status_code = 409
    return {
        "message": str(exception)
    }

@exception_view_config(HTTPForbidden,renderer='json')
@exception_view_config(UnAuthorized, renderer='json')
def forbidden(exception, request):
    request.response.status_code = 403
    return {
        "message":"Not authorized"
    }

# @exception_view_config(Exception, renderer='json')
# def forbidden(exception, request):
#     request.response.status_code = 500
#     return {
#         "message":str(exception)
#     }