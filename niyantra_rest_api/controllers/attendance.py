from pyramid.view import view_config

from niyantra_rest_api.services import BaseService, AttendanceService
from niyantra_rest_api.schemas import AttendanceSchema,AttendeeSchema
from niyantra_rest_api.models import Attendee
from niyantra_rest_api import constants

attendance_service = AttendanceService()

@view_config(route_name='attendance', request_method='GET',response_schema=AttendanceSchema)
def get_attendance(request):
    attendance_service.set_request(request)
    attendance = attendance_service.all()
    return attendance

@view_config(route_name='attendance', request_method='POST', schema=AttendanceSchema,response_schema=AttendanceSchema)
def mark_attendance(request):
    attendance = request.validated
    attendance_service.set_request(request)
    attendance = attendance_service.mark_attendance(attendance)
    return attendance