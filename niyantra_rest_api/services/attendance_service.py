from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

from niyantra_rest_api.services import BaseService
from niyantra_rest_api.models import Attendance,Section,AttendanceSheet,SectionSession,Student
from niyantra_rest_api.exceptions import ConstraintError

from sqlalchemy.orm import joinedload



class AttendanceService(BaseService):
    def __init__(self):
        super(AttendanceService,self).__init__(AttendanceSheet)

    def all(self):
        return self.dbsession.query(AttendanceSheet).options((
            joinedload(AttendanceSheet.section_session)).
            options(joinedload(AttendanceSheet.attendances).
            joinedload(Attendance.student))).all()

    def mark_attendance(self,attendance_sheet_id,attendance):
        attendance_sheet = self.get(attendance_sheet_id)
        if attendance_sheet is None:
            raise ConstraintError("No Attendance sheet found with this Id")

        student = self.get(attendance.student_id,model_class=Student)
        if student is None:
            raise ConstraintError("No student found with this Id")

        try:
            _attendance = self.dbsession.query(Attendance).filter_by(
                student=student, attendance_sheet=attendance_sheet).one()
            attendance.id = _attendance.id
            self.update(attendance.id, attendance, model_class=Attendance)
            return _attendance
        except NoResultFound:
            attendance.student = student
            attendance.attendance_sheet = attendance_sheet
            self.create(attendance)
        return attendance