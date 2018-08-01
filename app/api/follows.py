from flask import request, jsonify, g
from app import db
from app.schema.user_schema import user_schema, users_schema
from ..models.user import User
from ..models.follow import Follow
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
        f = Follow(follower_id=g.user.id, following_id=target.id)
        db.session.add(f)
        db.session.commit()
        return common_response(status=200)

    @staticmethod
    @login_required
    def unfollow(uuid):
        '''follow a user my personal info'''
        target = User.query.filter(User.uuid == uuid).first()
        f = Follow.query.filter(Follow.following_id == target.id).filter(Follow.follower_id == g.user.id).first()
        db.session.remove(f)
        db.session.commit()
        return common_response(status=200)

    @staticmethod
    @login_required
    def following():
        '''follow a user my personal info'''
        user_ids = Follow.query.filter(Follow.follower_id == g.user.id)
        users = User.query.filter(User.id == user_ids).all()
        return common_response(status=200, object=users_schema.dumps(users).data)

    @staticmethod
    @login_required
    def followers():
        '''follow a user my personal info'''
        user_ids = Follow.query.filter(Follow.following_id == g.user.id)
        users = User.query.filter(User.id == user_ids).all()
        return common_response(status=200, object=users_schema.dumps(users).data)

