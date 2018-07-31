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
        User.query.delete()
        Group.query.delete()
        News.query.delete()

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
            for i in range(1,4):
                group = Group(name=faker.city(), user_id=user.id)
                db.session.add(group)
                db.session.commit()

        with open('seed/news.json') as f:
            data = json.load(f)

        for i in range(1,10):
            news_json = data[i]
            news = News(user_id=matt_user.id,title = news_json['title'], url=news_json["url"])
            db.session.add(news)
        db.session.commit()






seed()
