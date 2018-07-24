from flask import Blueprint

apiv1 = Blueprint('v1',__name__  )

from .news import *
