from pyramid.view import view_config

from niyantra_rest_api.services import BaseService
from niyantra_rest_api.schemas import AttendeeSchema
from niyantra_rest_api.models import Attendee
from niyantra_rest_api import constants

attendee_service = BaseService(Attendee)

@view_config(route_name='attendee', request_method='GET',response_schema=AttendeeSchema)
def get_attendees(request):
    attendee_service.set_request(request)
    attendees = attendee_service.all()
    return attendees

@view_config(route_name='attendee', request_method='POST', schema=AttendeeSchema,response_schema=AttendeeSchema)
def create_attendee(request):
    attendee = request.validated
    attendee_service.set_request(request)
    return attendee_service.create(attendee)

@view_config(route_name='attendee_param', request_method='GET', response_schema=AttendeeSchema)
def get_attendee(request):
    attendee_service.set_request(request)
    return attendee_service.get(int(request.matchdict['id']))


@view_config(route_name='attendee_param', request_method='PUT', response_schema=AttendeeSchema)
def get_attendee(request):
    attendee = request.validated
    attendee_service.set_request(request)
    return attendee_service.get(int(request.matchdict['id']),attendee)


@view_config(route_name='attendee_param', request_method='DELETE', response_schema=AttendeeSchema)
def get_attendee(request):
    attendee_service.set_request(request)
    attendee_service.delete(int(request.matchdict['id']))
    request.response.status_code = 204
    return constants.EMPTY_STRING