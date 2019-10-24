from pyramid.view import view_config

from niyantra_rest_api.services import BaseService, AttendanceService
from niyantra_rest_api.schemas import AttendanceSchema,StudentSchema,AttendanceSheetSchema
from niyantra_rest_api.models import Section
from niyantra_rest_api import constants
from niyantra_rest_api.exceptions import NoResourceFound

attendance_service = AttendanceService()

@view_config(route_name='attendance_sheet', request_method='GET',response_schema=AttendanceSheetSchema)
def get_attendance_sheets(request):
    attendance_service.set_request(request)
    return attendance_service.all()

@view_config(route_name='attendance_sheet', request_method='POST', schema=AttendanceSheetSchema,response_schema=AttendanceSheetSchema)
def create_attendance_sheet(request):
    attendance_sheet = request.validated
    attendance_service.set_request(request)
    return attendance_service.create(attendance_sheet)

@view_config(route_name='attendance', request_method='POST', schema=AttendanceSchema,response_schema=AttendanceSchema)
def mark_attendance(request):
    attendance = request.validated
    attendance_service.set_request(request)
    attendance_sheet_id = request.matchdict['attendance_sheet_id']
    return attendance_service.mark_attendance(attendance_sheet_id, attendance)

@view_config(route_name='attendance', request_method='GET',response_schema=AttendanceSheetSchema)
def get_attendance_sheet(request):
    attendance = request.validated
    attendance_service.set_request(request)
    attendance_sheet_id = request.matchdict['attendance_sheet_id']
    attendance_sheet = attendance_service.get(attendance_sheet_id)
    if attendance_sheet is None:
        raise NoResourceFound
    return attendance_sheet
