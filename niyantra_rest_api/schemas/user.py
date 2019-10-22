from marshmallow import Schema,fields,post_load

class LoginSchema(Schema):
    username = fields.String(require=True)
    password = fields.String(require=True)
    remember_me = fields.Boolean()

class UserSchema(Schema):
    username = fields.String()
    fullname = fields.String()
    password = fields.String(load_only=True)
    email = fields.Email()

class UserTokenSchema(Schema):
    user = fields.Nested(UserSchema)
    token = fields.String(dump_only=True)

