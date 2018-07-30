from sqlalchemy import Column, Integer, String, Text, event
import uuid
import requests
from bs4 import BeautifulSoup
from app.models import db
from .dogear_model import DogearMixin
from ..util import get_domain_for_url


class News(DogearMixin, db.Model):
    __tablename__ = 'news'

    id = Column(Integer(), primary_key=True)
    title = Column(String)
    picture_url = Column(String)
    source = Column(String)
    url = Column(Text)
    user_id = Column(Integer())

    #soft_delete


    def __init__(self, user_id, title, url, picture_url="", source=None):
        '''Create the new news artcile'''

        self.uuid=str(uuid.uuid4())
        self.user_id=user_id
        self.title=title
        self.url = url

        self.update_with_details()

    def __repr__(self):
        return u'<News %s, %s>'.format(self.title, self.url)



    def as_dict(self):
        data = {'id': self.id}
        data.update(self.title)
        return data



    def update_with_details(self):
        #todo move this into celery
        url = self.url
        print(self.title)
        print(self.url)

        result = requests.get(url)
        soup = BeautifulSoup(result.content, "html.parser")
        for tag in soup.find_all("meta"):
            if tag.get("property", None) == "og:image":
                image = tag.get("content", None)
                if "http" not in image:
                    domain = get_domain_for_url(url)
                    image = domain + image
                self.picture_url = image


    @staticmethod
    def validate(data):

        if data["title"]==None or data["title"]=="":
            return False


        #todo check for unique
        return True






