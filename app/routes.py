from .api import apiv1
from .api.news import *
from .api.user import *
from .api.group import *
from .api.auth import get_auth_token, register





class Route():

    def __init__(self):
        ''''''

    @staticmethod
    def build(apiv1):


        apiv1.add_url_rule('/news','index', NewsController.index, methods=['GET'])
        apiv1.add_url_rule('/news', 'create', NewsController.create, methods=['POST'])

        apiv1.add_url_rule('/me', 'me', UserController.me, methods=['GET'])
        apiv1.add_url_rule('/users', 'put', UserController.update, methods=['POST'])

        apiv1.add_url_rule('/groups', 'groups', GroupController.index, methods=['GET'])
        apiv1.add_url_rule('/groups', 'create_group', GroupController.create, methods=['POST'])
        apiv1.add_url_rule('/groups', 'update_group', GroupController.update, methods=['PUT'])
        apiv1.add_url_rule('/groups', 'delete_group', GroupController.index, methods=['DELETE'])
        apiv1.add_url_rule('/groups/<string:uuid>', 'show_group', GroupController.show, methods=['GET'])
        #
        apiv1.add_url_rule('/get_auth_token', 'get_auth_token', get_auth_token,methods=['GET', 'POST'])
        apiv1.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])



        return apiv1