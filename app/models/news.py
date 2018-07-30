from sqlalchemy import Column, Integer, String, Text
import uuid

from app.models import db
from .dogear_model import DogearMixin


class News(DogearMixin, db.Model):
    __tablename__ = 'news'

    id = Column(Integer(), primary_key=True)
    title = Column(String)
    picture_url = Column(String)
    source = Column(String)
    url = Column(Text)
    user_id = Column(Integer())

    #soft_delete
    #flagged


    def __init__(self, user_id, title, url, picture_url="", source=None):
        '''Create the new news artcile'''
        super().__init__()
        self.uuid=str(uuid.uuid4())
        self.user_id=user_id
        self.title=title
        self.url = url
        self.picture_url = picture_url
        self.source = source

    def __repr__(self):
        return u'<News %s, %s>'.format(self.title, self.url)

    def as_dict(self):
        data = {'id': self.id}
        data.update(self.title)
        return data

    @staticmethod
    def validate(data):
        if data["title"]==None or data["title"]=="":
            return False
        return True
