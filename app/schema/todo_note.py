from marshmallow import Schema, fields


class AddNoteSchema(Schema):
    short_desc = fields.Str(required=True)
    description = fields.Str(required=False)
    plan_start = fields.DateTime(required=False)
    plan_finish = fields.DateTime(required=False)


class UpdateNoteSchema(Schema):
    short_desc = fields.Str(required=False)
    description = fields.Str(required=False)
    plan_start = fields.DateTime(required=False)
    plan_finish = fields.DateTime(required=False)
