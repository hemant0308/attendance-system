from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

from app.services.base_service import BaseService
from app.services.teacher_service import TeacherService
from app.models import Attendance,Section,AttendanceSheet,SectionSession,Student, AttendanceSheetStatus
from app.exceptions import ConstraintError, AttendanceSubmitted, UnAuthorized, DuplicateEntry
from app.utils import get_user_id

from sqlalchemy.orm import joinedload

teacher_service = TeacherService()

class AttendanceService(BaseService):
    def __init__(self):
        super(AttendanceService,self).__init__(AttendanceSheet)

    def all(self):
        return self.dbsession.query(AttendanceSheet).options(
            joinedload(AttendanceSheet.section_session)).all()

    def get(self, id):
        try:
            return self.dbsession.query(AttendanceSheet).options(
                joinedload(AttendanceSheet.section_session)).options(
                joinedload(AttendanceSheet.attendances).
                joinedload(Attendance.student)).filter(AttendanceSheet.id == id).one()
        except NoResultFound:
            return None

    def create(self, attendance_sheet):
        session = attendance_sheet.section_session
        if not self.request.is_admin:
            teacher = teacher_service.get_current_teacher()
            try:
                self.dbsession.query(TeacherSession).filter_by(teacher_id = teacher.id,section_session_id=session.id).one()
            except NoResultFound:
                raise UnAuthorized('You are not authorized')
        try:
            self.dbsession.query(AttendanceSheet).filter_by(date=attendance_sheet.date,section_session_id=attendance_sheet.section_session_id).one()
            raise DuplicateEntry('Attendance sheet is already created for this session on this date')
        except NoResultFound:
            return super().create(attendance_sheet)


    def mark_attendance(self,attendance_sheet_id,attendance):
        attendance_sheet = self.get(attendance_sheet_id)

        if not self.request.is_admin and attendance_sheet.created_by != self.request.authenticated_userid:
            raise UnAuthorized('You are not authorized to edit this sheet')

        if attendance_sheet.status == AttendanceSheetStatus.SUBMITTED:
            raise AttendanceSubmitted('Submitted attendance cannot be edited')

        if attendance_sheet is None:
            raise ConstraintError('No Attendance sheet found with this Id')

        student = super().get(attendance.student_id,model_class=Student)

        if student is None:
            raise ConstraintError('No student found with this Id')

        if student.section_id != attendance_sheet.section_session.section_id:
            raise ConstraintError('This student is not belongs to this session')

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
        if attendance_sheet.status == AttendanceSheetStatus.SUBMITTED:
            raise AttendanceSubmitted('Attendance Submitted Already')
        attendance_sheet.status = AttendanceSheetStatus.SUBMITTED
        attendance_sheet.submitted_by = get_user_id(self.request)
        attendance_sheet.submitted_on = datetime.now()
        self.save(attendance_sheet)