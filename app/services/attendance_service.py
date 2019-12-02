from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

from app.services.base_service import BaseService
from app.services.teacher_service import TeacherService
from app.models import Attendance,Section,AttendanceSheet,SectionSession,Student, AttendanceSheetStatus
from app.exceptions import ConstraintError, UnAuthorized, DuplicateEntry
from app.utils import get_user_id

from sqlalchemy.orm import joinedload

teacher_service = TeacherService()

class AttendanceService(BaseService):
    def __init__(self):
        super(AttendanceService,self).__init__(AttendanceSheet)

    def set_request(self, request):
        super().set_request(request)
        teacher_service.set_request(request)

    def all(self):
        return self.dbsession.query(AttendanceSheet).join(AttendanceSheet.section_session).join(SectionSession.section).filter(Section.school_id==self.request.school_id).all()

    def get(self, id):
        try:
            attendance_sheet = self.dbsession.query(AttendanceSheet).options(
                joinedload(AttendanceSheet.attendances).
                joinedload(Attendance.student)).join(AttendanceSheet.section_session).join(SectionSession.session).filter_by(id == id, Section.school_id == self.request.school_id).one()
            self._check_current_school(attendance_sheet)
            if(not self.request.is_admin):
                teacher = teacher_service.get_current_teacher()
        except NoResultFound:
            return None

    def _check_is_current_school(self, attendance_sheet):
        session = super().get(attendance_sheet.section_session_id, model_class=SectionSession)
        section = session.section
        super().has_access_to_school(section.school_id)

    def _has_access_to_section_session(self,section_session_id):
        teacher = teacher_service.get_current_teacher()
        try:
            self.dbsession.query(TeacherSession).filter_by(teacher_id = teacher.id,section_session_id=section_session_id).one()
        except NoResultFound:
            raise UnAuthorized('You dont have access to create attendance sheet to given session')

    def create(self, attendance_sheet):
        self.is_current_school(attendance_sheet)
        if not self.request.is_admin:
            section_session_id = attendance_sheet.section_session_id
            self._has_access_to_section_session(section_session_id)
        try:
            self.dbsession.query(AttendanceSheet).filter_by(date=attendance_sheet.date,section_session_id=attendance_sheet.section_session_id).one()
            raise DuplicateEntry(f"Attendance sheet is already created for given session on {attendance_sheet.date}")
        except NoResultFound:
            return super().create(attendance_sheet)

    def mark_attendance(self,attendance_sheet_id,attendance):
        attendance_sheet = self.get(attendance_sheet_id)

        if attendance_sheet is None:
            raise ConstraintError('No Attendance sheet found with given Id.')

        self._check_is_current_school(attendance_sheet)

        if not self.request.is_admin and attendance_sheet.created_by != self.request.authenticated_userid:
            raise UnAuthorized('You dont have access to edit this attendance sheet.')

        if attendance_sheet.status == AttendanceSheetStatus.SUBMITTED:
            raise UnAuthorized('Submitted attendance cannot be edited.')

        student = super().get(attendance.student_id,model_class=Student)

        if student is None:
            raise ConstraintError('No student found with given studentId.')

        if student.section_id != attendance_sheet.section_session.section_id:
            raise ConstraintError('Given studentId is not belongs to given attendance sheet\'s session.')

        try:
            _attendance = self.dbsession.query(Attendance).filter_by(
                student=student, attendance_sheet=attendance_sheet).one()
            attendance.id = _attendance.id
            self.update(attendance.id, attendance, model_class=Attendance)
            return _attendance
        except NoResultFound:
            attendance.student = student
            attendance.attendance_sheet = attendance_sheet
            super().create(attendance)
        return attendance

    def submit(self, attendance_sheet_id):
        attendance_sheet = self.get(attendance_sheet_id)

        self._check_current_school(attendance_sheet)

        if attendance_sheet.status == AttendanceSheetStatus.SUBMITTED:
            raise UnAuthorized('Attendance corresponding to given Id, Submitted Already.')
        attendance_sheet.status = AttendanceSheetStatus.SUBMITTED
        attendance_sheet.submitted_by = get_user_id(self.request)
        attendance_sheet.submitted_on = datetime.now()
        self.save(attendance_sheet)