from .api import apiv1
from .api.news import *
from .api.user import *
from .api.auth import login, register

class Route():

    def __init__(self):
        ''''''

    @staticmethod
    def build(apiv1):


        apiv1.add_url_rule('/news','index', NewsController.index, methods=['GET'])
        apiv1.add_url_rule('/news', 'create', NewsController.create, methods=['POST'])

        apiv1.add_url_rule('/me', 'me', UserController.me, methods=['GET'])
        apiv1.add_url_rule('/users', 'put', UserController.update, methods=['POST'])

        apiv1.add_url_rule('/login', 'login', login,methods=['GET', 'POST'])
        apiv1.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])



        return apiv1