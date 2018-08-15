from flask import request, jsonify, g
from . import apiv1
from ..models.news import News
from ..models.user import User
from app import db
from .auth import login_required
from ..schema.schemas import *
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

        news = db.session.query(News).order_by("created_at desc").all()
        return common_response(object=newses_schema.dump(news).data)

    @staticmethod
    @login_required
    def share():
        req_data = request.get_json()
        news_id = req_data["news_id"]
        group_ids_array = req_data["group_ids"]
        for id in group_ids_array:

            pass
            #for each group id, get the users and send the feed item to their feed

    @staticmethod
    @login_required
    def full_news_feed():
        followers = g.user.followers.all()
        ids = [user.id for user in followers]
        if len(ids)==0:
            feed = News.query.order_by("created_at desc").limit(50).all()
        else:
            feed = News.query.filter(News.user_id==ids).order_by("created_at desc").all()
        return common_response(object=newses_schema.dump(feed).data)

    @staticmethod
    def public_feed():
        feed = News.query.all()
        return common_response(object=newses_schema.dump(feed).data)

    @staticmethod
    @login_required
    def user_news_feed(uuid):
        user = User.query.filter(User.uuid==uuid).first()
        feed = user.user_news_feed()
        return common_response(object=newses_schema.dump(feed).data)

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

        try:
            news = News(title=req_data["title"], url=req_data["url"], user_id=g.user.id)
            db.session.add(news)
            db.session.commit()
            return common_response(object=news_schema.dump(news).data)

        except AssertionError as message:
            db.session.rollback()
            return common_response(status=400, message=message, token="")



