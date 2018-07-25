from flask_marshmallow import Marshmallow
from marshmallow import fields
ma = Marshmallow()
from ..models.news import News

class NewsSchema(ma.Schema):
    class Meta:
        model = News

        fields = ('uuid','title', 'url')
    title = fields.String()
    url = fields.String()
    user_id = fields.Integer()

    # Smart hyperlinking
    # _links = ma.Hyperlinks({
    #     'self': ma.URLFor('user_detail', id='<id>'),
    #     'collection': ma.URLFor('users')
    # })


news_schema = NewsSchema()
newses_schema = NewsSchema(many=True)