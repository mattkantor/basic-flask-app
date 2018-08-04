from marshmallow import Schema, fields
from ..models.user import User

class UserSchema(Schema):
    class Meta:
        model = User

        fields = ( 'username', 'avatar')


    username = fields.String()
    avatar = fields.String()



    #
    # _links = Hyperlinks({
    #     'self': ma.URLFor('user_detail', id='<id>'),
    #     'collection': ma.URLFor('users')
    # })


user_schema = UserSchema()
users_schema = UserSchema(many=True)