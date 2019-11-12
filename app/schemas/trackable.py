from marshmallow import fields,Schema,post_load,validates_schema,ValidationError

class TrackableSchema(Schema):
    created_at = fields.DateTime(dump_only=True)
    created_by = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    updated_by = fields.String(dump_only=True)
