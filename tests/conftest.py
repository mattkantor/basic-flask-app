import pytest
import sys
from app import create_app
from app.models.news import db as _db
from tests.client import ApiTestingResponse

print("loaded conftest", sys.stdout)

@pytest.yield_fixture(scope='session')
def app():

    app = create_app(config='../config/testing.py')
    app.response_class = ApiTestingResponse
    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.yield_fixture(scope='session')
def db(app):
    #_db.drop_all()
    print("dbcreate", sys.stderr)
    _db.drop_all()
    _db.create_all()
    #return _db

    yield _db


    #print("db done", sys.stderr)

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.yield_fixture(scope='function')
def session(db):

    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection)
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
