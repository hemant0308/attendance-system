from pyramid.view import view_config, view_defaults

from app.services import SectionService
from app.models import Section
from app.schemas import SectionSchema, SectionSessionSchema, StudentSchema
from app.constants import Permissions

section_service = SectionService()

@view_defaults(permission=Permissions.authenticated_only)
class SectionController():
    def __init__(self, request):
        self.request = request
        section_service.set_request(request)

    @view_config(route_name='section', request_method='GET',response_schema=SectionSchema)
    def all(self):
        return section_service.all()

    @view_config(route_name='section', request_method='POST', schema=SectionSchema, permission=Permissions.admin_only, response_schema=SectionSchema)
    def create(self):
        session = self.request.validated
        session.school_id = self.request.school_id
        return section_service.create(session)

    @view_config(route_name='section_session', request_method='POST',permission=Permissions.admin_only, schema=SectionSessionSchema,response_schema=SectionSessionSchema)
    def add_session(self):
        session = self.request.validated
        section_id = self.request.matchdict['section_id']
        return section_service.add_session(section_id, session)

    @view_config(route_name='section_session', request_method='GET',response_schema=SectionSessionSchema)
    def get_sessions(self):
        section_id = self.request.matchdict['section_id']
        return section_service.get_sessions(section_id)

    @view_config(route_name='section_student', request_method='GET',response_schema=StudentSchema)
    def get_students(self):
        section_id = int(self.request.matchdict['section_id'])
        return section_service.get_students(section_id)

