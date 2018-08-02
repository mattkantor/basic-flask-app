
from marshmallow import Schema, fields

from ..models.group import Group

class GroupSchema(Schema):
    class Meta:
        model = Group

        fields = ('uuid','name', "user_ids")
    uuid = fields.String()
    name = fields.String()
    user_ids = fields.String()





group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)