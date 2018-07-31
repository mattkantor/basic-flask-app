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
    factories.MeFactory.create_batch(1)

    response = client.post('/api/v1/groups', data=json.dumps({"name":"test"}), headers = headers)
    print(response.json)
    assert response.status_code !=200


def test_add_a_new_group(client, session):
    factories.MeFactory.create_batch(1)

    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }
    response = client.post('/api/v1/groups',  data=json.dumps({"name":"test gorup"}),headers = headers)
    assert response.status_code == 200



def test_get_my_groups(client, session):
    factories.MeFactory.create_batch(1)
    factories.GroupFactory._create_batch(3)
    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }

    client.post('/api/v1/groups', data=json.dumps({"name": "test mygroup"}), headers=headers)
    response = client.get('/api/v1/groups',headers = headers)
    assert response.status_code == 200
    assert len(response.json["data"]) == 1


@skip("none")
def test_add_user_to_group(client, session):
    factories.MeFactory.create_batch(1)
    factories.GroupFactory.create_batch(3)
    user = User.query.first()

    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }
    response = client.get('/api/v1/groups', headers=headers)

    group0 = response.json["data"]
    print(group0)


    group_id = group0['uuid']
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }
    data = json.dumps({"user_uuid":user.uuid})
    grp_url = '/api/v1/groups/'+str(group_id)+'/add_user'

    print(grp_url)
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