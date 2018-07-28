from tests import factories

username="mattkantor"
password = "password"
email = "matthewkantor@msn.com"

def test_should_create_a_new_valid_user(client, session):

    response = client.get('/api/v1/register', data=dict(username=username, password=password, email=email))

    assert response.status_code == 200
    assert len(response.json) == 1

def test_should_not_create_a_user(client, session):

    response = client.post('/api/v1/register', data=dict(username="dddadsfas", email="fff@ff.com", password=""))
    assert response.status_code != 200
    response = client.post('/api/v1/register', data=dict(username="a;slKDJa", email="", password="dddadsfas"))
    assert response.status_code != 200
    response = client.post('/api/v1/register', data=dict(username="", email="joe@joe.com", password="dddadsfas"))
    assert response.status_code != 200

def test_can_get_a_new_auth_token(client, session):
    response = client.post('/api/v1/get_auth_token',
                           data=dict(email=email, password=password))


    assert len(response.json) == 1
    assert len(response.json["token"])>50

