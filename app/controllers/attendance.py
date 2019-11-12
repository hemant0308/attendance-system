from pyramid.view import view_config,view_defaults

from niyantra_rest_api.services import BaseService, AttendanceService
from niyantra_rest_api.schemas import AttendanceSchema,StudentSchema,AttendanceSheetSchema
from niyantra_rest_api.models import Section
from niyantra_rest_api import constants
from niyantra_rest_api.exceptions import ResourceNotFound
from niyantra_rest_api.utils import set_empty_response
from niyantra_rest_api.constants import Permissions

attendance_service = AttendanceService()
attendance_sheet_schema = AttendanceSheetSchema()
attendance_schema = AttendanceSchema()

@view_defaults(permission=Permissions.admin_only)
class AttendanceController(object):

    def __init__(self, request):
        self.request = request
        attendance_service.set_request(request)

    @view_config(route_name='attendance_sheet', request_method='GET',response_schema=AttendanceSheetSchema)
    def get_attendance_sheets(self):
        return attendance_service.all()

    @view_config(route_name='attendance_sheet', request_method='POST', schema=AttendanceSheetSchema,response_schema=AttendanceSheetSchema)
    def create_attendance_sheet(self):
        attendance_sheet = self.request.validated
        return attendance_service.create(attendance_sheet)

    @view_config(route_name='attendance', request_method='POST', schema=AttendanceSchema,response_schema=AttendanceSchema)
    def mark_attendance(self):
        attendance = self.request.validated
        attendance_sheet_id = self.request.matchdict['attendance_sheet_id']
        return attendance_service.mark_attendance(attendance_sheet_id, attendance)

    @view_config(route_name='attendance', request_method='GET',response_schema=AttendanceSheetSchema)
    def get_attendance_sheet(self):
        attendance = self.request.validated
        attendance_sheet_id = self.request.matchdict['attendance_sheet_id']
        attendance_sheet = attendance_service.get(attendance_sheet_id)
        if attendance_sheet is None:
            raise ResourceNotFound
        res = attendance_sheet_schema.dump(attendance_sheet)
        res['attendances'] = attendance_schema.dump(attendance_sheet.attendances,many=True)
        return res

    @view_config(route_name='submit_attendance', request_method='POST')
    def submit_attendance(self):
        attendance_sheet_id = self.request.matchdict['attendance_sheet_id']
        attendance_service.submit(attendance_sheet_id)
        return set_empty_response(request)