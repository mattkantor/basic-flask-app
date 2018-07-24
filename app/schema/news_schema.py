from flask_marshmallow import Marshmallow
ma = Marshmallow()

class NewsSchema(ma.Schema):
    class Meta:

        fields = ('uuid','title', 'url')
    # Smart hyperlinking
    # _links = ma.Hyperlinks({
    #     'self': ma.URLFor('user_detail', id='<id>'),
    #     'collection': ma.URLFor('users')
    # })

user_schema = NewsSchema()
users_schema = NewsSchema(many=True)