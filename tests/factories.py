import factory
import uuid

import pytest
from factory import PostGenerationMethodCall
from faker import Faker
from app.models.user import User
from app.models.group import Group
from app.models.news import db, News

faker = Faker()

def get_authable_email():
    return "matt.kantor@gmail.com"

def get_authable_username():
    return "mattkantor"


class SQLAlchemyModelFactory(factory.Factory):

    class Meta:
        abstract = True

    @classmethod
    def create_batch(cls, size,  **kwargs):


        return [cls.create(**kwargs) for _ in range(size)]

    @classmethod
    def cleanup(cls):
        #if cls._meta.model:
        db.session.query(cls._meta.model).delete()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = db.session
        session.begin(nested=True)
        #session.query(model_class).delete()
        obj = model_class(*args, **kwargs)

        session.add(obj)
        session.commit()
        return obj



class MeFactory(SQLAlchemyModelFactory):

    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: get_authable_username())
    #uuid = factory.LazyAttribute(lambda x: str(uuid.uuid4()))
    email = factory.LazyAttribute(lambda x: get_authable_email())
    password = PostGenerationMethodCall('set_password', 'password')




class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x:"sally"+ faker.last_name())
    #uuid = factory.LazyAttribute(lambda x: str(uuid.uuid4()))
    email = factory.LazyAttribute(lambda x: faker.email())
    password = PostGenerationMethodCall('set_password', 'password')#



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
