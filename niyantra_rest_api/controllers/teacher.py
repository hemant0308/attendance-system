from pyramid.view import view_config

from niyantra_rest_api.services import TeacherService
from niyantra_rest_api.models import Teacher
from niyantra_rest_api.schemas import TeacherSchema, TeacherSessionSchema
from niyantra_rest_api import constants
from niyantra_rest_api.utils import set_empty_response
from niyantra_rest_api.constants import Permissions

teacher_service = TeacherService()

@view_config(permission=Permissions.admin_only, name='teacher_controller')
class TeacherController():
    def __init__(self, request):
        self.request = request
        teacher_service.set_request(request)

    @view_config(route_name='teacher', request_method='GET',response_schema=TeacherSchema)
    def get_teachers(self):
        return teacher_service.all()

    @view_config(route_name='teacher', request_method='POST', schema=TeacherSchema, response_schema=TeacherSchema)
    def create_teacher(self):
        teacher = self.request.validated
        return teacher_service.create(teacher)

    @view_config(route_name='teacher_session', request_method='GET', response_schema=TeacherSessionSchema)
    def get_sessions(self):
        teacher_id = self.request.matchdict['teacher_id']
        sessions = teacher_service.get_sessions(teacher_id)
        return sessions

    @view_config(route_name='teacher_session', request_method='POST', schema=TeacherSessionSchema, response_schema=TeacherSessionSchema)
    def add_session(self):
        teacher_id = self.request.matchdict['teacher_id']
        teacher_session = self.request.validated
        return teacher_service.add_session(teacher_id, teacher_session)
    