from flask import request, jsonify
from flask import g
from app.schema.group_schema import groups_schema, group_schema
from . import apiv1, login_required
from app.models import *
from .api_helper import *

class GroupController():
    def __init__(self):
        ''''''

    @staticmethod
    @login_required
    def index():
        '''show all groups'''
        groups = Group.query.filter(Group.user_id==g.user.id).all()
        return common_response(object=groups_schema.dump(groups))


    @staticmethod
    @login_required
    def show(uuid):
        '''create a groups'''
        group = Group.query.filter(Group.uuid == uuid).first()
        return common_response(object=group_schema.dump(group))


    @staticmethod
    @login_required
    def create():
        '''create a groups'''
        req_data = request.get_json()
        name = req_data["name"]
        group = Group(name=name, user_id = g.user.id)
        db.session.add(group)
        db.session.commit()
        return common_response(object=group_schema.dump(group))


    @staticmethod
    @login_required
    def update():
        '''create a groups'''

    @staticmethod
    @login_required
    def delete():
        '''create a groups'''

    @staticmethod
    @login_required
    def add_user():
        '''add a user'''

    @staticmethod
    @login_required
    def remove_user():
        '''remove user from group'''

