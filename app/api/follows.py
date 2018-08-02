from flask import request, jsonify, g, json
from app import db
from app.schema.user_schema import user_schema, users_schema
from ..models.user import User
# from ..models.follow import Follow
from . import apiv1, login_required, News
from .api_helper import *

class FollowController():
    def __init__(self):
        pass

    @staticmethod
    @login_required
    def follow(uuid):
        '''follow a user my personal info'''


        target = User.query.filter(User.uuid == uuid).first()
        g.user.follow(target)
        db.session.commit()
        return common_response(status=200)

    @staticmethod
    @login_required
    def unfollow(uuid):
        '''follow a user my personal info'''
        target = User.query.filter(User.uuid == uuid).first()
        g.user.unfollow(target)
        db.session.commit()
        return common_response(status=200)

    @staticmethod
    @login_required
    def following():
        '''fwho am I following'''
        users = g.user.followed.all()
        data = users_schema.dumps(users).data

        return common_response(status=200, object=data)

    @staticmethod
    @login_required
    def followers():
        '''whos is following me'''
        users = g.user.followers.all()
        return common_response(status=200, object=users_schema.dumps(users).data)

