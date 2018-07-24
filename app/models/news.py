from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text



migrate = Migrate()
db = SQLAlchemy()


class News(db.Model):
    id = Column(Integer(), primary_key=True)
    title = Column(String)
    picture_url = Column(String)
    source = Column(String)
    url = Column(Text)

    def __init__(self, data):
        ''''''

    def __repr__(self):
        return u'<News %s>'.format(self.title)

    def as_dict(self):
        data = {'id': self.id}
        data.update(self.title)
        return data
