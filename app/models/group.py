from sqlalchemy import Column, Integer, String, Text, ForeignKey
import uuid

from sqlalchemy.orm import relationship

from .dogear_model import DogearMixin
from .user import *
from app.models import db
from sqlalchemy.dialects.postgresql import ARRAY



class Group(DogearMixin, db.Model):

    __tablename__ = "groups"

    id = Column(Integer(), primary_key=True)
    name = Column(String)
    user_id = Column(Integer, nullable=False)
    #user_ids = Column(ARRAY(Integer))
    #user = relationship('User')

    def __init__(self, name=name, user_id=user_id):
        self.name = name
        self.user_id = user_id
        self.uuid = str(uuid.uuid4())


    def add_user_to_group(self,user_uuid):
        pass

    def remove_user_to_group(self, user_uuid):
        pass


