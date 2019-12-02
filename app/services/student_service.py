from .base_service import BaseService
from app.models import Student,Section

class StudentService(BaseService):
    def __init__(self):
        super(StudentService, self).__init__(Student)

    def all(self):
        return self.dbsession.query(Student).optoins(joinload(Student.section)).filter(Section.school_id == self.request.school_id).all()

    def create(self, student):
        section = self.dbsession.query(Section).filter(Section.id == student.section_id)
        if section is None:
            raise NoResourceFound('No Section found with given id.')
        self.has_access_to_school(section.school_id)
        super().create(student)