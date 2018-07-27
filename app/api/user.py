from flask import request, jsonify
from . import apiv1, login_required


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
        return jsonify({'user': 'current_user'})

    @staticmethod
    @login_required
    def search(**kwargs):
        '''returns info afor users matching a search'''

    @staticmethod
    @login_required
    def update():
        '''updates my personal info'''



