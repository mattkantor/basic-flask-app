
from sqlalchemy import Column, Integer, String, Text, ForeignKey,  Boolean
from sqlalchemy.orm import backref, relationship

from app.models import DogearMixin, db


# class Follow( DogearMixin,db.Model):
#     __tablename__ = 'follows'
#
#     id = Column(Integer(), primary_key=True, autoincrement=True)
#     follower_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
#     following_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
#
#     following = relationship("User", backref=backref("following", cascade="all, delete-orphan"))
#
#     followers = relationship("User", backref=backref("followers", cascade="all, delete-orphan"))
#
#     def __init__(self, follower_id=follower_id, following_id=following_id):
#         self.follower_id = follower_id
#         self.following_id = following_id
