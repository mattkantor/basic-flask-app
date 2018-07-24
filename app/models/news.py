from sqlalchemy import Column, Integer, String, Text
from uuid import UUID
from .dogear_model import DogearModel


class News(DogearModel):
    id = Column(Integer(), primary_key=True)
    uuid = Column(String)
    title = Column(String)
    picture_url = Column(String)
    source = Column(String)
    url = Column(Text)
    user_id = Column(Integer())

    def __init__(self, user_id, title, url, picture_url="", source=None):
        '''Create the new news artcile'''
        super.__init__()
        self.user_id=user_id
        self.title=title
        self.url = url
        self.picture_url = picture_url
        self.source = source

    def __repr__(self):
        return u'<News %s>'.format(self.title)

    def as_dict(self):
        data = {'id': self.id}
        data.update(self.title)
        return data
