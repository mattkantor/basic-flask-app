import pytest
from pytest import skip
from sqlalchemy.testing.config import skip_test

from app import User
from tests import factories
from flask import json
from faker import Faker

from tests.factories import get_authable_email, get_authable_username
from tests.test_helper import get_token

username=get_authable_username()
password = "password"
email = get_authable_email()


mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}




def test_add_group_without_auth(client, session):
    factories.UserFactory.cleanup()
    factories.MeFactory.create_batch(1)

    response = client.post('/api/v1/groups', data=json.dumps({"name":"test"}), headers = headers)

    assert response.status_code !=200


def test_add_a_new_group(client, session):
    factories.UserFactory.cleanup()
    factories.MeFactory.create_batch(1)

    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }
    response = client.post('/api/v1/groups',  data=json.dumps({"name":"test gorup"}),headers = headers)
    assert response.status_code == 200
    factories.UserFactory.cleanup()


def test_get_my_groups(client, session):
    factories.UserFactory.cleanup()
    factories.GroupFactory.cleanup()

    me = factories.MeFactory(username=get_authable_username(), email=get_authable_email())


    #factories.GroupFactory._create_batch(3)

    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }

    #first create a group
    client.post('/api/v1/groups', data=json.dumps({"name": "test mygroup"}), headers=headers)

    #now get it
    response = client.get('/api/v1/groups',headers = headers)
    assert response.status_code == 200
    assert len(response.json["data"]) == 1
    factories.UserFactory.cleanup()


def test_add_user_to_group(client, session):
    factories.UserFactory.cleanup()
    factories.GroupFactory.cleanup()
    me = factories.MeFactory(username=get_authable_username(), email=get_authable_email())
    users = factories.UserFactory.create_batch(3)
    group = factories.GroupFactory(user_id=me.id, name="my test groupio") #pass in userid


    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }
    # response = client.get('/api/v1/groups/' + group.uuid, headers=headers)
    #
    #
    #
    # group_id = group.uuid
    # headers = {
    #     'Content-Type': mimetype,
    #     'Accept': mimetype,
    #     "Authorization": "Bearer " + token
    # }
    data = json.dumps({"user_uuid":users[0].uuid})
    grp_url = '/api/v1/groups/'+str(group.uuid)+'/add_user'


    response = client.post(grp_url,headers = headers, data = data)
    assert response.status_code == 200



#
# def test_add_self_to_group(client, session):
#     token = get_token(client, session)
#     headers = {
#         'Content-Type': mimetype,
#         'Accept': mimetype,
#         "Authorization": "Bearer " + token
#     }
#     response = client.get('/api/v1/groups/:id/add_user/:user_id',headers = headers)
#     assert response.status_code == 200
#     assert len(response.json) == 1
#
#
# def test_delete_user_from_group(client, session):
#     token = get_token(client, session)
#     headers = {
#         'Content-Type': mimetype,
#         'Accept': mimetype,
#         "Authorization": "Bearer " + token
#     }
#     response = client.post('/api/v1/group/:id/del_user/:user_id')
#
#     assert response.status_code == 200
#     assert len(response.json) == 1