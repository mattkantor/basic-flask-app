from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
db = SQLAlchemy()
from .feed import *
from .news import *
from .user import *
from .group import *
from .follow import *
