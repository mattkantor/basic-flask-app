from flask import json
from pytest import skip
import pytest

from tests import factories
from tests.factories import get_authable_username, get_authable_email

from tests.test_helper import get_token

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}


def test_follow_user(client, session):

    users = factories.UserFactory.create_batch(3)
    me = factories.MeFactory(username=get_authable_username(), email=get_authable_email())
    users.append(me)

    uuid = users[0].uuid


    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }
    # response = client.get('/api/v1/users/search?query=sally' , headers=headers)
    # assert len(response.json["data"]) >0
    #
    # print(response.json["data"][0])
    # user_uuid = "12341234123"

    response = client.get('/api/v1/follow/'+ uuid, headers=headers)
    assert response.status_code == 200
    factories.UserFactory.cleanup()
