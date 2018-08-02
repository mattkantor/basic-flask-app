from _md5 import md5

from sqlalchemy import Column, Integer, String, Text, ForeignKey,  Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, validates, backref
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import uuid
import app
import jwt
import re
from flask import current_app as app

from app.models import DogearMixin, db, News

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))
)


class User( DogearMixin,db.Model):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)

    news = db.relationship('News', backref='user', lazy='dynamic')
    groups = db.relationship('Group', backref='user', lazy='dynamic')

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    @hybrid_property  #placeholder
    def avatar(self,size=128):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def __init__(self, email=email, username="", password=""):
        self.uuid = str(uuid.uuid4())
        self.email = email
        self.username = username

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def user_news_feed(self):
        followed = News.query.join(
            followers, (followers.c.followed_id == News.user_id)).filter(
            followers.c.follower_id == self.id)
        own = News.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(News.created_at.desc())


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






