from flask import request, jsonify, g
from . import apiv1
from ..models.news import News
from app import db
from .auth import login_required
from ..schema.news_schema import *
from .api_helper import *

class NewsController():
    def __init__(self):
        ''''''

    @staticmethod
    @login_required
    def index():
        '''Returns all the news for a user
        Call this api passing a user key
        ---

        responses:
          500:
            description: Error The language is not awesome!
          200:
            description: A language with its awesomeness
            schema:
              id: News
              properties:
                title:
                  type: string
                  description: The article name
                  default: None
                image:
                  type: base/64
                  description: Image representing the news item

                  '''

        news = db.session.query(News).all()
        return common_response(object=newses_schema.dump(news))


    @staticmethod
    @login_required
    def create():
        '''Create a news for a user
                Call this api passing a user key
                ---

                responses:
                  500:
                    description: Meh, we're broken!
                  200:
                    description: News created!
                    schema:
                      id: awesome
                      properties:
                        title:
                          type: string
                          description: The article name
                          default: None
                        image:
                          type: base/64
                          description: Image representing the news item

                          '''
        #todo validate
        req_data = request.get_json()

        if not News.validate(req_data):
            return common_response(status=500,message='invalid record')


        news = News(title=req_data["title"], url=req_data["title"], user_id=g.user.id)
        db.session.add(news)
        db.session.commit()
        return common_response(object=news_schema.dump(news))



