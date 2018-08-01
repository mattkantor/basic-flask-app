from flask import json
from pytest import skip

from tests import factories


from tests.test_helper import get_token

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}


def test_add_news_without_auth(client, session):
    factories.UserFactory.cleanup()
    factories.MeFactory.create_batch(1)
    token = get_token(client, session)

    url="http://cnn.com/"

    response = client.post('/api/v1/news',data=dict(url=url))
    assert response.status_code == 401
    factories.UserFactory.cleanup()

def test_add_news_with_auth(client, session):

    factories.UserFactory.cleanup()
    factories.MeFactory.create_batch(1)
    token = get_token(client, session)
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": "Bearer " + token
    }


    url="http://cnn.com/"

    response = client.post('/api/v1/news',data=json.dumps({"url":url, "title":"this is the title"}), headers=headers)
    assert response.status_code == 200





