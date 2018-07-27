from flask_marshmallow import Marshmallow
from marshmallow import fields
ma = Marshmallow()
from ..models.group import Group

class GroupSchema(ma.Schema):
    class Meta:
        model = Group

        fields = ('uuid','name')
    uuid = fields.String()
    name = fields.String()



    # Smart hyperlinking
    # _links = ma.Hyperlinks({
    #     'self': ma.URLFor('user_detail', id='<id>'),
    #     'collection': ma.URLFor('users')
    # })


group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)