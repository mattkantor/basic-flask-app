from flask import request, jsonify
from . import apiv1
from ..models.news import News
from app import db
from flask_login import login_user, logout_user, current_user, login_required
from ..schema.news_schema import *

class NewsController():
    def __init__(self):
        ''''''

    @login_required
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

        news = db.session.query(News).all()
        return jsonify({'news': newses_schema.dump(news)})

    @login_required
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
        #todo validate
        data = request.form
        if not News.validate(data):
            resp= jsonify({'message':'invalid record','news': None})
            resp.status_code = 500
            return resp

        news = News(title=data["title"], url=data["title"], user_id=1)
        db.session.add(news)
        db.session.commit()
        return jsonify({'news': dict(title=data["title"], url=data["url"])})


