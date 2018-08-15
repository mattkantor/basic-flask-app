from marshmallow import Schema, fields
from ..models.news import News
from ..models.group import Group
from ..models.user import User

class NewsSchema(Schema):

    class Meta:
        model = News

        fields = ('uuid','title', 'url','picture_url', 'author')
    uuid = fields.String()
    title = fields.String()
    url = fields.String()
    picture_url = fields.String()
    user_id = fields.Integer()
    author = fields.Nested('UserSchema', many=False, exclude=('news',))

news_schema = NewsSchema()
newses_schema = NewsSchema(many=True)


class UserSchema(Schema):
    class Meta:
        model = User

        fields = ( 'username', 'avatar', 'about', 'geo','news')


    username = fields.String()
    avatar = fields.String()
    about = fields.String()
    geo = fields.String()
    news = fields.Nested(NewsSchema, many=True, exclude=("user",))



user_schema = UserSchema()
users_schema = UserSchema(many=True)


class GroupSchema(Schema):
    class Meta:
        model = Group

        fields = ('uuid','name', "user_ids")
    uuid = fields.String()
    name = fields.String()
    user_ids = fields.String()


group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)