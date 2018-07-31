from flask import request, jsonify, g
from app import db
from app.schema.user_schema import user_schema, users_schema
from ..models.user import User
from ..models.follow import Follow
from . import apiv1, login_required, News
from .api_helper import *

class UserController():
    def __init__(self):
        ''''''

    @staticmethod
    @login_required
    def me():
        '''my personal profile
                ---
                responses:
                  500:
                    description: you must not exist!!
                  200:
                    description: Your user profile
                    schema:
                      id: User
                      properties:
                        username:
                          type: string
                          description: The user name
                          default: None
                        avatar:
                          type: base/64
                          description: your avatar'''
        news = []
        user = User.query.filter(User.id == g.user.id).first()

        return common_response( object=user_schema.dump(user).data)

    @staticmethod
    @login_required
    def search():
        '''search users
                       ---
                       responses:
                         500:
                           description: search has caused an error!!
                         200:
                           description: list of user profile
                           schema:
                             id: Users
                             properties:
                               username:
                                 type: string
                                 description: The user name
                                 default: None
                               email:
                                 type: string
                                 description: your avatar'''

        query = request.args.get("query")
        #tod - search on what?
        users = User.query.all()
        return common_response(object=users_schema.dump(users).data)


    @staticmethod
    @login_required
    def show(uuid):
        if uuid =="":
            return common_response(status=404)

        user = User.query.filter(User.uuid == uuid).first()

        news = News.query.filter(News.user_id==user.id).all()

        return common_response(object=user_schema.dump(user).data)


    @staticmethod
    @login_required
    def update():
        '''updates my personal info'''

    @staticmethod
    @login_required
    def follow(uuid):
        '''follow a user my personal info'''
        target = User.query.filter(User.uuid==uuid).first()
        f = Follow(follower_id=g.user.id, following_id=target.id)
        db.session.add(f)
        db.session.commit()
        return common_response(status=200)


    @staticmethod
    @login_required
    def unfollow(uuid):
        '''follow a user my personal info'''
        target = User.query.filter(User.uuid == uuid).first()
        f = Follow.query.filter(Follow.following_id==target.id).filter(Follow.follower_id==g.user.id).first()
        db.session.remove(f)
        db.session.commit()
        return common_response(status=200)

    @staticmethod
    @login_required
    def following():
        '''follow a user my personal info'''
        user_ids = Follow.query.filter(Follow.follower_id==g.user.id)
        users = User.query.filter(User.id==user_ids).all()
        return common_response(status=200, object=users_schema.dumps(users).data)

    @staticmethod
    @login_required
    def followers():
        '''follow a user my personal info'''
        user_ids = Follow.query.filter(Follow.following_id == g.user.id)
        users = User.query.filter(User.id == user_ids).all()
        return common_response(status=200, object=users_schema.dumps(users).data)
