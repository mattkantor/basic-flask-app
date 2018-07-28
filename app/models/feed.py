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



class Feed(db.Model, DogearMixin):
    __tablename__ = 'feed'
    __table_args__ = {"schema": "public"}

    id = Column(Integer(), primary_key=True)
    uuid = Column(String())
    from_user_id = Column(Integer())
    user_id = Column(Integer())
    from_group_id = Column(Integer())
    news_id = Column(Integer())


    def __init__(self, from_user_id=from_user_id, from_group_id=from_group_id, user_id=user_id, news_id=news_id):
        self.uuid = str(uuid.uuid4())
        self.from_user_id = from_user_id
        self.from_group_id = from_group_id
        self.user_id = user_id
        self.news_id = news_id

    def feed_for_user(self, user_id):
        return Feed.query.filter(Feed.user_id==user_id).all()



