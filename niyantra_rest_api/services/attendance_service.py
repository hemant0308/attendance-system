from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

from niyantra_rest_api.services import BaseService
from niyantra_rest_api.models import Attendance,Attendee
from niyantra_rest_api.exceptions import ConstraintError


class AttendanceService(BaseService):
    def __init__(self):
        super(AttendanceService,self).__init__(Attendance)

    def mark_attendance(self, attendance):
        attendee = self.get(attendance.attendee_id,model_class=Attendee)
        if attendee is None:
            raise ConstraintError("No Attendee found with this Id")
        try:
            _attendance = self.dbsession.query(Attendance).filter_by(
                date=attendance.date,attendee=attendee).one()
            attendance.created_at = datetime.now()
            attendance.id = _attendance.id
            attendance.attendee = attendee
            self.dbsession.merge(attendance)
        except NoResultFound:
            attendance.attendee = attendee
            attendance.created_at = datetime.now()
            self.dbsession.add(attendance)
        self.flush()
        return attendance