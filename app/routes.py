from .api import apiv1
from .api.news import *

class Route():

    def __init__(self):
        ''''''

    @staticmethod
    def build( apiv1):


        apiv1.add_url_rule('/news','index', News.index, methods=['GET'])
        apiv1.add_url_rule('/news', 'create', News.create, methods=['POST'])





        return apiv1