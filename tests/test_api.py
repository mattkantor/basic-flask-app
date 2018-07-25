from tests import factories


def test_get_should_return_bs_news(client, session):

    response = client.get('/api/v1/news')

    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_should_create_news(client, session):

    response = client.post('/api/v1/news', data=dict(title="Test News", url="http://cbc.ca", picture_url="http://microsoft.com"))

    assert response.status_code == 200

    assert len(response.json) == 1
    assert response.json["news"]["title"] == "Test News"


def test_get_did_create_a_bunch_of_news(client, session):
    response = client.post('/api/v1/news',
                           data=dict(title="Test News 2", url="http://cbc.ca", picture_url="http://microsoft.com"))
    response = client.post('/api/v1/news',
                           data=dict(title="Test News 3", url="http://bbc.co.uk", picture_url="http://microsoft.com"))
    response = client.post('/api/v1/news',
                           data=dict(title="Test News 4", url="this is not a url", picture_url="http://microsoft.com"))


    response = client.get('/api/v1/news')
    assert len(response.json["news"][0]) == 4

def test_did_not_create_invalid_news_objects(client, session):
    response = client.post('/api/v1/news',
                           data=dict( url="Im not a url", picture_url="im also not a url"))

    assert len(response.json["news"]) == 0