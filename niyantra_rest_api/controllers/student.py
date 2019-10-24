from pyramid.view import view_config

from niyantra_rest_api.services import BaseService
from niyantra_rest_api.schemas import StudentSchema
from niyantra_rest_api.models import Student
from niyantra_rest_api import constants

student_service = BaseService(Student)

@view_config(route_name='student', request_method='GET',response_schema=StudentSchema)
def get_students(request):
    student_service.set_request(request)
    students = student_service.all()
    return students

@view_config(route_name='student', request_method='POST', schema=StudentSchema,response_schema=StudentSchema)
def create_student(request):
    student = request.validated
    student_service.set_request(request)
    return student_service.create(student)

@view_config(route_name='student_param', request_method='GET', response_schema=StudentSchema)
def get_student(request):
    student_service.set_request(request)
    return student_service.get(int(request.matchdict['id']))


@view_config(route_name='student_param', request_method='PUT', response_schema=StudentSchema)
def get_student(request):
    student = request.validated
    student_service.set_request(request)
    return student_service.get(int(request.matchdict['id']),student)


@view_config(route_name='student_param', request_method='DELETE', response_schema=StudentSchema)
def get_student(request):
    student_service.set_request(request)
    student_service.delete(int(request.matchdict['id']))
    request.response.status_code = 204
    return constants.EMPTY_STRING