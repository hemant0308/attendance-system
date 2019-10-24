
from .base_service import BaseService
from niyantra_rest_api.models import Section, SectionSession
from niyantra_rest_api.exceptions import ConstraintError


class SectionService(BaseService):
    def __init__(self):
        super(SectionService,self).__init__(Section)

    def add_session(self, section_id ,session):
        section = self.get(section_id)
        if section is None:
            raise ConstraintError("No Attendance group is found with this id")
        session.section = section
        return self.create(session)

    def get_sessions(self, section_id):
        return self.dbsession.query(SectionSession).filter(
            SectionSession.section_id == section_id).all()