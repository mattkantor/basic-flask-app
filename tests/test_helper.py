from flask import json

from tests import factories
from tests.factories import get_authable_email
from tests.test_api import mimetype


def get_token(client, session, password="password"):


    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = client.post('/api/v1/get_auth_token', headers=headers,
                          data=json.dumps({ "password": "password", "email": get_authable_email()}))

    print(response.json)
    return response.json["token"]