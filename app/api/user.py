from flask import request, jsonify, g
from ..schema.schemas import *
from ..models.user import User

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
                   description: list of user profiles
                   schema:
                     id: User'''


        query = request.args.get('query')
        users = User.query.filter(User.username.ilike('%'+query+'%')).all()
        return common_response(object=users_schema.dump(users).data)


    @staticmethod
    #@login_required
    def show(username):
        if username =="":
            return common_response(status=404)

        user = User.query.filter(User.username == username).first()

        news = user.news

        return common_response(object=user_schema.dump(user).data)


    @staticmethod
    @login_required
    def update():
        '''updates my personal info'''
