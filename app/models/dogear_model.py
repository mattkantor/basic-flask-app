from sqlalchemy import Column, Integer, String, Text, DateTime, func
from uuid import UUID

from sqlalchemy.ext.declarative import declared_attr



class DogearMixin(object):

    uuid = Column(String)
    created_at = Column(DateTime, default=func.now())



