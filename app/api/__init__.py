from flask import Blueprint

apiv1 = Blueprint('v1',__name__  )
app_routes = Blueprint('app',__name__  )

from .news import *
from .user import *
from .feed import *
from .group import *
