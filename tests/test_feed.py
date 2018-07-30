from pytest import skip

from tests import factories
from flask import json

username="mattkantor"
password = "password"
email = "matthewkantor@msn.com"

@skip
def test_should_create_a_new_valid_user(client, session):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = client.get('/api/v1/register', data=json.dumps({"username":username, "password": password, "email": email}))

    assert response.status_code == 200
    assert len(response.json) == 1