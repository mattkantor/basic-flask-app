from pytest import skip

from tests import factories
from flask import json
from faker import Faker



username="mattkantor_groups"
password = "password"
email = "matthewkantor+groups@msn.com"

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}


def setup_user(client, session):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = client.get('/api/v1/register',headers=headers, data=json.dumps({"username":username, "password":password, "email":email}))

    token = response.json["token"]
    return token

def get_token(client, session):
    setup_user(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = client.get('/api/v1/get_auth_token', headers=headers,
                          data=json.dumps({ "password": password, "email": email}))

    return response.json["token"]


def test_add_group_without_auth(client, session):



    response = client.post('/api/v1/groups', data=json.dumps({"name":"test"}), headers = headers)
    print(response.json)
    assert response.status_code !=200


def test_add_a_new_group(client, session):
    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }
    response = client.post('/api/v1/groups',  data=json.dumps({"name":"test gorup"}),headers = headers)
    assert response.status_code == 200



def test_get_my_groups(client, session):
    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }
    response = client.get('/api/v1/groups',headers = headers)
    assert response.status_code == 200



# def test_add_user_to_group(client, session):
#     token = get_token(client, session)
#     headers = {
#         'Content-Type': mimetype,
#         'Accept': mimetype,
#         "Authorization": "Bearer " + token
#     }
#     response = client.post('/api/v1/group/:id/add_user/:user_id',headers = headers)
#     assert response.status_code == 200
#     assert len(response.json) == 1
#
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