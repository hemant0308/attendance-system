from pyramid.view import view_config

from niyantra_rest_api.services import SectionService
from niyantra_rest_api.models import Section
from niyantra_rest_api.schemas import SectionSchema, SectionSessionSchema
from niyantra_rest_api import constants

section_service = SectionService()

@view_config(route_name='section', request_method='GET',response_schema=SectionSchema)
def all(request):
    section_service.set_request(request)
    return section_service.all()

@view_config(route_name='section', request_method='POST', schema=SectionSchema,response_schema=SectionSchema)
def create(request):
    session = request.validated
    section_service.set_request(request)
    return section_service.create(session)

@view_config(route_name='section_session', request_method='POST', schema=SectionSessionSchema,response_schema=SectionSessionSchema)
def add_session(request):
    session = request.validated
    section_service.set_request(request)
    section_id = request.matchdict['section_id']
    return section_service.add_session(section_id, session)

@view_config(route_name='section_session', request_method='GET',response_schema=SectionSessionSchema)
def get_sessions(request):
    section_service.set_request(request)
    section_id = request.matchdict['section_id']
    return section_service.get_sessions(section_id)