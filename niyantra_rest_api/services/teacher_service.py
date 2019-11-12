from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound
from .base_service import BaseService
from .user_service import UserService
from niyantra_rest_api.models import Teacher,SectionSession,TeacherSession
from niyantra_rest_api.exceptions import DuplicateEntry
from niyantra_rest_api import constants

user_service = UserService()

class TeacherService(BaseService):
    def __init__(self):
        super(TeacherService,self).__init__(Teacher)

    def create(self, teacher):
        username = teacher['username']
        user_service.set_request(self.request)
        user = user_service.create_user({
            'username':teacher['username'],
            'password':constants.TEACHER_DEFAULT_PASSWORD,
            'fullname':teacher['fullname'],
            'roles':['TEACHER']})
        teacher = Teacher()
        teacher.user = user
        return super().create(teacher)

    def get_sessions(self, teacher_id):
        teacher = self.get(teacher_id)
        sessions = self.dbsession.query(TeacherSession).options(
            joinedload(TeacherSession.section_session).joinedload(SectionSession.section)).filter(TeacherSession.teacher == teacher).all()
        return sessions

    def get_current_teacher(self):
        user_id = self.request.authenticated_userid
        return self.dbsession.query(Teacher).filter(Teacher.user_id == user_id).one()

    def add_session(self, teacher_id, teacher_session):
        try:
            teacher_session = self.dbsession.query(TeacherSession).filter_by(teacher_id=teacher_id,section_session_id = teacher_session.section_session_id).one()
            raise DuplicateEntry("This session is already added to this teacher")
        except NoResultFound:
            teacher_session.teacher_id = teacher_id
            return super().create(teacher_session)

    def get_current_teacher(self):
        userid = self.request.authenticated_userid
        return self.dbsession.query(Teacher).filter(Teacher.user_id == userid).one()