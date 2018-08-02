import random

import requests
import json

from flask import Flask

from app import create_app, init_app
from app.models import *
from faker import Faker

faker = Faker()
valid_email = "matthewkantor@gmail.com"
valid_password = "password"
valid_user = "mattkantor"

app = create_app()


def seed():
    with app.app_context():

        Group.query.delete()
        News.query.delete()
        users = User.query.all()
        for user in users:
            db.session.delete(user)
        db.session.commit()


        matt_user = User(email=valid_email, username=valid_user)
        matt_user.set_password(valid_password)
        db.session.add(matt_user)
        db.session.commit()

        for i in range(1,5):

            user = User(email=faker.email(), password="password", username=faker.first_name())
            user.set_password(valid_password)
            db.session.add(user)
            db.session.commit()
            uuid = user.uuid
            if i % 2 ==0:
                matt_user.follow(user)
                db.session.commit()
            random.seed(10)
            with open('seed/news.json') as f:
                data = json.load(f)
                for j in range(1,3):

                    news_json = data[random.randint(0, 10)]
                    news = News(user_id=matt_user.id, title=news_json['title'], url=news_json["url"])
                    db.session.add(news)
                db.session.commit()


            for i in range(1,4):
                group = Group(name=faker.city(), user_id=user.id)
                db.session.add(group)
                db.session.commit()










seed()
