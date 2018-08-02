from sqlalchemy import Column, Integer, String, Text, ForeignKey
import uuid

from sqlalchemy.orm import relationship

from .dogear_model import DogearMixin
from .user import *
from app.models import db
from sqlalchemy.dialects.postgresql import ARRAY



class Group(DogearMixin, db.Model):

    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = db.Column(Integer, db.ForeignKey('users.id'))
    user_ids = Column(ARRAY(Integer), default=[])
    #user = relationship('User')

    def __init__(self, name=name, user_id=user_id):
        self.name = name
        self.user_id = user_id
        self.uuid = str(uuid.uuid4())


    def add_user_to_group(self,user_uuid):
        user_ids = self.user_ids
        user_ids.append(user_uuid)
        self.user_ids = list(set(user_ids))

        return True, "OK"

    def remove_user_to_group(self, user_uuid):
        user_ids = self.user_ids
        user_ids.remove(user_uuid)
        self.user_ids = list(set(user_ids))
        return True, "OK"


