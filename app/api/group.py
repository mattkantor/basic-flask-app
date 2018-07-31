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
        data = groups_schema.dump(groups).data

        return common_response(object=data)


    @staticmethod
    @login_required
    def show(uuid):
        '''create a groups'''
        group = Group.query.filter(Group.uuid == uuid).first()
        data=group_schema.dump(group).data
        return common_response(object=data)


    @staticmethod
    @login_required
    def create():
        '''create a groups'''
        req_data = request.get_json()
        name = req_data["name"]
        group = Group(name=name, user_id = g.user.id)
        db.session.add(group)
        db.session.commit()
        data = group_schema.dump(group).data
        return common_response(object=data)


    @staticmethod
    @login_required
    def update():
        '''create a groups'''
        return common_response(status=200, message="OK")

    @staticmethod
    @login_required
    def delete():
        '''create a groups'''
        return common_response(status=200, message="OK")

    @staticmethod
    @login_required
    def add_user(uuid):
        '''add a user'''
        req_data = request.get_json()
        user_uuid = req_data["user_uuid"]
        group = Group.query.filter(Group.uuid==uuid).first()
        success = False
        message="OK"
        try:
            if group:
                success, message = group.add_user_to_group(user_uuid)

            if success==True:
                status = 200
            else:
                status = 400

            return common_response(status=status, message=message)
        except AssertionError as message:
            db.session.rollback()
            return common_response(status=400, message=message, token="")

    @staticmethod
    @login_required
    def remove_user():
        '''remove user from group'''
        return common_response(status=200, message="OK")
