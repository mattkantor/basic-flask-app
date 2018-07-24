from tests import factories


def test_get_should_return_bs_news(client, session):

    response = client.get('/api/v1/news')

    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_should_create_news(client, session):

    response = client.post('/api/v1/news', data=dict(title="Test News", url="http://cbc.ca", picture_url="http://microsoft.com"))

    assert response.status_code == 200
    assert len(response.json) == 1

