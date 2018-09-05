from flask import request, jsonify, g, json
from app import db
from ..schema.schemas import *
from ..models.user import User
# from ..models.follow import Follow
from . import apiv1, login_required, News
from .api_helper import *

class FollowController():
    def __init__(self):
        pass

    @staticmethod
    @login_required
    def follow(username):
        '''follow user
               ---
               responses:
                 500:
                   description: search has caused an error!!
                 200:
                   description: list of user profiles
                   schema:
                     id: User'''


        target = User.query.filter(User.username == username).first()
        g.user.follow(target)
        db.session.commit()
        return common_response(status=200)

    @staticmethod
    @login_required
    def unfollow(username):
        '''follow a user my personal info'''
        target = User.query.filter(User.username == username).first()
        g.user.unfollow(target)
        db.session.commit()
        return common_response(status=200)

    @staticmethod
    @login_required
    def following():
        '''fwho am I following'''
        users = g.user.followed.all()
        data = users_schema.dump(users).data
        return common_response(status=200, object=data)

    @staticmethod
    @login_required
    def followers():
        '''whos is following me'''
        users = g.user.followers.all()
        return common_response(status=200, object=users_schema.dump(users).data)

