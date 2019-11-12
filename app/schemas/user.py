from marshmallow import Schema,fields,post_load
from app.models import LoginUser,Role

class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    remember_me = fields.Boolean()

class UserSchema(Schema):
    username = fields.String(required=True)
    fullname = fields.String(required=True)
    password = fields.String(load_only=True, required=True)
    roles = fields.List(fields.String, required=True, many=True, load_only=True)
    email = fields.Email()
    id = fields.Int(dump_only=True)
