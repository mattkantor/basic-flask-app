from flask.ext.migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from sqlalchemy import Column, Integer, String, Text



migrate = Migrate()
db = SQLAlchemy()


class User(db.Model):
    id = Column(Integer(), primary_key=True)
    username = Column(String)


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
