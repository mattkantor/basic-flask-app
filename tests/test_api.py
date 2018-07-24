from tests import factories


def test_get_should_return_documents(client, session):

    response = client.get('/api/v1/news')

    assert response.status_code == 200
    assert len(response.json) == 1


