from flask import json
from pytest import skip

from tests import factories
from tests.factories import get_authable_username, get_authable_email
from tests.test_helper import get_token

mimetype = 'application/json'

def test_search_for_users(client, session):
    factories.UserFactory.cleanup()
    me = factories.MeFactory(username=get_authable_username(), email=get_authable_email())
    factories.UserFactory(username="johnsmith", email="johnsmith@gmail.com", password="password")
    factories.UserFactory(username="johnsmith2", email="john2smith@gmail.com", password="password")
    factories.UserFactory(username="johnsmith3", email="john3smith@gmail.com", password="password")

    token = get_token(client, session)

    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }

    response = client.get('/api/v1/users/search?query=john', headers=headers)
    assert response.status_code ==200
    assert len(response.json["data"])==3