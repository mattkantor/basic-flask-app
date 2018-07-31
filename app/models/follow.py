
from sqlalchemy import Column, Integer, String, Text, ForeignKey,  Boolean

from app.models import DogearMixin, db


class Follow( DogearMixin,db.Model):
    __tablename__ = 'follows'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    follower_id = Column(Integer(), nullable=False)
    following_id = Column(Integer(), nullable=False)

    def __init__(self, follower_id=follower_id, following_id=following_id):
        self.follower_id = follower_id
        self.following_id = following_id
