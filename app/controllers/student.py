from pyramid.view import view_config, view_defaults

from app.services import StudentService
from app.schemas import StudentSchema, SectionSchema
from app.models import Student
from app import constants
from app.utils import set_empty_response
from app.exceptions import ResourceNotFound
from app.constants import Permissions

student_service = StudentService()

student_schema = StudentSchema()
section_schema = SectionSchema()

@view_defaults(permission=Permissions.authenticated_only)
class StudentController():
    def __init__(self, request):
        self.request = request
        student_service.set_request(request)

    @view_config(route_name='student', request_method='GET')
    def get_students(self):
        _students = student_service.all()
        students = []
        for _student in _students:
            student = student_schema.dump(_student)
            student['section'] = section_schema.dump(_student.section)
            students.append(student)
        return students

    @view_config(route_name='student', request_method='POST', schema=StudentSchema,response_schema=StudentSchema)
    def create_student(self):
        student = self.request.validated
        return student_service.create(student)

    @view_config(route_name='student_param', request_method='GET')
    def get_student(self):
        student = student_service.get(int(self.request.matchdict['student_id']))
        if student is None:
            raise ResourceNotFound
        student_dict = student_schema.dump(student)
        student_dict['section'] = section_schema.dump(student.section)
        return student_dict

    @view_config(route_name='student_param', schema=StudentSchema, request_method='PUT', response_schema=StudentSchema)
    def update_student(self):
        student = self.request.validated
        return student_service.update(int(self.request.matchdict['student_id']), student)

    @view_config(route_name='student_param', request_method='DELETE', response_schema=StudentSchema)
    def delete_student(self):
        student_service.delete(int(self.request.matchdict['student_id']))
        return set_empty_response(self.request)