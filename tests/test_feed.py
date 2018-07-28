from tests import factories

username="mattkantor"
password = "password"
email = "matthewkantor@msn.com"

def test_should_create_a_new_valid_user(client, session):

    response = client.get('/api/v1/register', data=dict(username=username, password = password, email = email))

    assert response.status_code == 200
    assert len(response.json) == 1