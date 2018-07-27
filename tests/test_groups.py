from tests import factories


def test_add_group_witoout_auth(client, session):
    response = client.post('/api/v1/groups')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_add_a_new_group(client, session):
    response = client.post('/api/v1/groups')
    assert response.status_code == 200
    assert len(response.json) == 1


def test_get_my_groups(client, session):
    response = client.get('/api/v1/groups')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_add_user_to_group(client, session):
    response = client.post('/api/v1/group/:id/add_user/:user_id')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_add_self_to_group(client, session):
    response = client.get('/api/v1/groups/:id/add_user/:user_id')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_delete_user_from_group(client, session):
    response = client.post('/api/v1/group/:id/del_user/:user_id')

    assert response.status_code == 200
    assert len(response.json) == 1