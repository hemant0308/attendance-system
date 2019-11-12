from .base_service import BaseService
from app.models import Student

class StudentService(BaseService):
    def __init__(self):
        super(StudentService, self).__init__(Student)

    def all(self):
        return self.dbsession.query(Student).optoins(joinload(Student.section)).filter_by(section_id = section_id).all()