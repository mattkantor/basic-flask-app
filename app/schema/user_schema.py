from flask_marshmallow import Marshmallow
from marshmallow import fields
ma = Marshmallow()
from ..models.user import User

class UserSchema(ma.Schema):
    class Meta:
        model = User

        fields = ('uuid','email', 'username', 'uuid')
    uuid = fields.String()
    email = fields.String()
    username = fields.String()



    # Smart hyperlinking
    # _links = ma.Hyperlinks({
    #     'self': ma.URLFor('user_detail', id='<id>'),
    #     'collection': ma.URLFor('users')
    # })


user_schema = UserSchema()
users_schema = UserSchema(many=True)