from tests import factories

username="mattkantor_groups"
password = "password"
email = "matthewkantor+groups@msn.com"

def setup(client, session):
    response = client.get('/api/v1/register', data=dict(username=username, password=password, email=email))

    assert response.status_code == 200
    assert len(response.json) == 1

    token = response.json["token"]
    return token

def test_add_group_witoout_auth(client, session):

    response = client.post('/api/v1/groups', data={"name":"test"})
    assert response.status_code == 200
    assert len(response.json) == 1

def test_add_a_new_group(client, session):
    token = setup(client, session)
    headers = {"Authorization": "Bearer " + token}
    response = client.post('/api/v1/groups',  data={"name":"test gorup"},headers = headers)
    assert response.status_code == 200
    assert len(response.json) == 1


def test_get_my_groups(client, session):
    token = setup(client, session)
    headers = {"Authorization": "Bearer " + token}
    response = client.get('/api/v1/groups',headers = headers)
    assert response.status_code == 200
    assert len(response.json) == 1

def test_add_user_to_group(client, session):
    token = setup(client, session)
    headers = {"Authorization": "Bearer " + token}
    response = client.post('/api/v1/group/:id/add_user/:user_id',headers = headers)
    assert response.status_code == 200
    assert len(response.json) == 1

def test_add_self_to_group(client, session):
    token = setup(client, session)
    headers = {"Authorization": "Bearer " + token}
    response = client.get('/api/v1/groups/:id/add_user/:user_id',headers = headers)
    assert response.status_code == 200
    assert len(response.json) == 1

def test_delete_user_from_group(client, session):
    token = setup(client, session)
    headers = {"Authorization": "Bearer " + token}
    response = client.post('/api/v1/group/:id/del_user/:user_id')

    assert response.status_code == 200
    assert len(response.json) == 1