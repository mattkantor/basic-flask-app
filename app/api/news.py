from flask import request, jsonify
from . import apiv1
from ..models.news import News
from app import db

class NewsController():
    def __init__(self):
        ''''''

    @staticmethod
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
        news = []
        return jsonify({'news': news})

    @staticmethod
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
        news = []
        data  =  request.form
        news = News(title=data["title"], url=data["title"], user_id=1)
        db.session.add(news)
        db.session.commit()
        return jsonify({'news': dict(title=data["title"], url=data["url"])})


