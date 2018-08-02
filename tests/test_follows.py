from flask import json
from pytest import skip
import pytest

from tests import factories
from tests.factories import get_authable_username, get_authable_email

from tests.test_helper import get_token

mimetype = 'application/json'



def test_follow_unfollow_user(client, session):

    users = factories.UserFactory.create_batch(3)
    me = factories.MeFactory(username=get_authable_username(), email=get_authable_email())
    users.append(me)

    uuid_to_follow = users[0].uuid


    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }


    response = client.get('/api/v1/follow/'+ uuid_to_follow, headers=headers)
    assert response.status_code == 200

    response = client.get('/api/v1/following', headers=headers)

    assert response.status_code == 200
    assert eval(response.json["data"]) != []


    response = client.get('/api/v1/unfollow/' + uuid_to_follow, headers=headers)
    assert response.status_code == 200

    response = client.get('/api/v1/following', headers=headers)

    assert response.status_code == 200
    assert eval(response.json["data"])==[] #todo why is thius eval() ????

    factories.UserFactory.cleanup()
