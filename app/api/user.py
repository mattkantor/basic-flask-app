from flask import request, jsonify
from . import apiv1



class UserController():
    def __init__(self):
        ''''''

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
        return jsonify({'user': {'username':'@blurrycam','about':'Likes to paint and do drywall','geo':'Toronto ON Canada'}})

    @staticmethod
    def update():
        '''updates my personal info'''

    @staticmethod
    def login():
        '''allows me to login'''
        news = []
        return jsonify({'news': {"name":"hi"}})



