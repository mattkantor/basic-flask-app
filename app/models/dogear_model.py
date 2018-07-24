from uuid import UUID
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy

migrate = Migrate()
db = SQLAlchemy()

class DogearModel(db.Model):

    def __init__(self):
        ''''''
        self.uuid = UUID.uuid4()


