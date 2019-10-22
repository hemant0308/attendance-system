from marshmallow import fields,Schema,post_load

from niyantra_rest_api.models import Attendee

class AttendeeSchema(Schema):
    id = fields.String()
    firstname = fields.String(required=True)
    lastname = fields.String()
    @post_load
    def get_obj(self,data,**kwargs):
        return Attendee(**data)