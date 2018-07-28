
from tests import factories

username="mattkantor"
password = "password"
email = "matthewkantor@msn.com"

def test_add_news_witoout_auth(client, session):


    url="http://cnn.com/"

    response = client.post('/api/v1/news',data=dict(url=url))
    assert response.status_code == 200


