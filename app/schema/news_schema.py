from marshmallow import Schema, fields

from app.schema.user_schema import UserSchema
from ..models.news import News

class NewsSchema(Schema):
    class Meta:
        model = News

        fields = ('uuid','title', 'url','picture_url', 'author')
    uuid = fields.String()
    title = fields.String()
    url = fields.String()
    picture_url = fields.String()
    user_id = fields.Integer()
    author = fields.Nested(UserSchema)

    # Smart hyperlinking
    # _links = ma.Hyperlinks({
    #     'self': ma.URLFor('user_detail', id='<id>'),
    #     'collection': ma.URLFor('users')
    # })


news_schema = NewsSchema()
newses_schema = NewsSchema(many=True)