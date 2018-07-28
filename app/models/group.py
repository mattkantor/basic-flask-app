from sqlalchemy import Column, Integer, String, Text, ForeignKey
import uuid

from sqlalchemy.orm import relationship

from .dogear_model import DogearMixin
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy
from .user import *
from sqlalchemy.dialects.postgresql import ARRAY

migrate = Migrate()
db = SQLAlchemy()

class Group(DogearMixin, db.Model):

    __tablename__ = "groups"
    __table_args__ = {"schema": "public"}

    id = Column(Integer(), primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('public.groups.user_id'),nullable=False)
    user_ids = Column(ARRAY(Integer))
    #user = relationship('User')

    def __init__(self, name=name, user_id=user_id):
        self.name = name
        self.user_id = user_id
        self.uuid = str(uuid.uuid4())


    def add_user_to_group(self,user_uuid):
        pass

    def remove_user_to_group(self, user_uuid):
        pass


