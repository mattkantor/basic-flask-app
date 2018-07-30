from flask.ext.migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from sqlalchemy import Column, Integer, String, Text, ForeignKey,  Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import uuid
import app
import jwt
import re
import os
import sys
from flask import current_app as app

from app.models import DogearMixin, db


class User( DogearMixin,db.Model):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
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
        if not password:
            raise AssertionError('Password is required to sign up')

        # if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
        #     raise AssertionError('Password must contain 1 capital letter and 1 number')

        if len(password) < 6 or len(password) > 50:
            raise AssertionError('Your Password must be between 6 and 50 characters')



        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')

        return email






