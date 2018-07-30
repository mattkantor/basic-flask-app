from flask.ext.migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from sqlalchemy import Column, Integer, String, Text, ForeignKey,  Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import uuid
import app
import jwt
import os
import sys
from flask import current_app as app

from .group import *


migrate = Migrate()
db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'


    id = Column(Integer(), primary_key=True)
    uuid = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    #groups = relationship("Group")

    def __init__(self, email=email, username="", password=""):
        self.uuid = str(uuid.uuid4())
        self.email = email
        self.username = username



    def encode_auth_token(self):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': self.uuid
            }

            print( app.config["SECRET_KEY"], file=sys.stderr)
            return jwt.encode(
                payload,
                app.config["SECRET_KEY"],
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            print( app.config["SECRET_KEY"])
            print(auth_token)
            payload = jwt.decode(auth_token, app.config["SECRET_KEY"],algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    @staticmethod
    def validate(args):
        print(args)

        email = args["email"]
        password = args["password"]

        if  email =="" or password=="":
            return False, "Blank Fields"
        if email ==None or password==None:
            return False, "No Data Provided "

        #check user
        exists = User.query.filter(User.email==email).first()
        if exists:
            return False, "Duplicate Email"
        # if username:
        #     exists2 = User.query.filter(User.username == username).first()
        #     if exists2:
        #         return False, "Username is already taken"

        return True, "OK"



        #check_password_hash(hash, 'foobar')


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)

