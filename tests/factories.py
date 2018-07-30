import factory
import uuid

import pytest
from faker import Faker
from app.models.user import User
from app.models.group import Group
from app.models.news import db, News

faker = Faker()


class SQLAlchemyModelFactory(factory.Factory):

    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = db.session
        session.begin(nested=True)
        obj = model_class(*args, **kwargs)
        session.add(obj)
        session.commit()
        return obj


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: faker.first_name())
    #uuid = factory.LazyAttribute(lambda x: str(uuid.uuid4()))
    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: User().set_password("Blahs"))

class GroupFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User

    name = factory.LazyAttribute(lambda x: "Blahs")
    #uuid = factory.LazyAttribute(lambda x: str(uuid.uuid4()))
    #TODO will break
    user_id = factory.LazyAttribute(lambda x: 1)
#
# class NewsFactory(SQLAlchemyModelFactory):
#
#     class Meta:
#         model = News
#
#     title = factory.LazyAttribute(lambda x: "Blahs")
#
#     uuid = factory.LazyAttribute(lambda x: str(uuid.uuid4()))
