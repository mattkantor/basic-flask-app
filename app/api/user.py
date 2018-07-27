from flask import request, jsonify, g
from . import apiv1, login_required
from .api_helper import *

class UserController():
    def __init__(self):
        ''''''
    @login_required
    @staticmethod
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
        return common_response( object=g.user)

    @staticmethod
    @login_required
    def search(**kwargs):
        '''returns info afor users matching a search'''

    @staticmethod
    @login_required
    def update():
        '''updates my personal info'''



