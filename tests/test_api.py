from pytest import skip
from sqlalchemy.testing.config import skip_test

from app import User
from tests import factories
from flask import json

from tests.factories import get_authable_email

username="mattskasntor"
password = "passsword"
email = "matthewdskantor@msn.com"

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}



def test_should_create_a_new_valid_user(client, session):
    #factories.MeFactory.create_batch(1)


    response = client.post('/api/v1/register', headers=headers,
                          data=json.dumps({"username": username, "password": password, "email": email}))

    assert response.status_code == 200



def test_should_not_create_a_user(client, session):

    response = client.post('/api/v1/register',headers=headers, data=dict(username="dddadsfas", email="fff@ff.com", password=""))
    assert response.status_code != 200
    response = client.post('/api/v1/register',headers=headers, data=dict(username="a;slKDJa", email="", password="dddadsfas"))
    assert response.status_code != 200
    response = client.post('/api/v1/register',headers=headers, data=dict(username="", email="joe@joe.com", password="dddadsfas"))
    assert response.status_code != 200


def test_can_get_a_new_auth_token(client, session):
    factories.MeFactory.create_batch(1)

    response = client.post('/api/v1/get_auth_token',headers=headers,
                           data=json.dumps({"email":get_authable_email(), "password":"password"}))



    assert len(response.json["token"])>50
#
