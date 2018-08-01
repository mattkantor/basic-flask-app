from flask import json
from pytest import skip

from tests import factories
from tests.test_helper import get_token

username="mattkantor"
password = "password"
email = "matthewkantor@msn.com"

@skip
def test_follow_and_unfollow_user(client, session):
    factories.UserFactory.cleanup()
    token = get_token(client, session)
    #need a token

    response = client.get('/api/v1/users/search',data=json.dumps({"query":"john"}))
    assert response.status_code == 401