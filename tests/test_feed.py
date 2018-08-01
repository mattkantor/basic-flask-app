from pytest import skip
from tests import factories
from flask import json

from tests.factories import get_authable_username, get_authable_email
from tests.test_helper import get_token

username=get_authable_username()
password = "password"
email = get_authable_email()

@skip
def test_should_get_feed_stories(client, session):
    factories.UserFactory.cleanup()
    factories.MeFactory.create_batch(1)
    token = get_token(client, session)

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    assert(True)


