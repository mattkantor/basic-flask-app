from app.api.feed import FeedController
from app.api.follows import FollowController
from .api import apiv1, app_routes

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
        apiv1.add_url_rule('/news_feed', 'full_user_news_feed', NewsController.full_news_feed   ,
                           methods=['GET'])

        app_routes.add_url_rule('/index.rss', 'rss_Feed', FeedController.rss,
                           methods=['GET'])

        apiv1.add_url_rule('/public_feed', 'public_feed', NewsController.public_feed,
                           methods=['GET'])

        apiv1.add_url_rule('/me', 'me', UserController.me, methods=['GET'])
        apiv1.add_url_rule('/users', 'put', UserController.update, methods=['POST'])
        apiv1.add_url_rule('/users/<string:username>', 'show', UserController.show, methods=['GET'])
        apiv1.add_url_rule('/users/search', 'search', UserController.search, methods=['GET'])

        apiv1.add_url_rule('/users/<string:uuid>/feed', 'user_news_feed', NewsController.user_news_feed, methods=['GET'])

        apiv1.add_url_rule('/follow/<string:username>', 'follow', FollowController.follow, methods=['GET'])
        apiv1.add_url_rule('/unfollow/<string:username>', 'unfollow', FollowController.unfollow, methods=['GET'])
        apiv1.add_url_rule('/followers', 'followers', FollowController.followers, methods=['GET'])
        apiv1.add_url_rule('/following', 'following', FollowController.following, methods=['GET'])

        apiv1.add_url_rule('/groups', 'groups', GroupController.index, methods=['GET'])
        apiv1.add_url_rule('/groups', 'create_group', GroupController.create, methods=['POST'])
        apiv1.add_url_rule('/groups', 'update_group', GroupController.update, methods=['PUT'])
        apiv1.add_url_rule('/groups', 'delete_group', GroupController.index, methods=['DELETE'])
        apiv1.add_url_rule('/groups/<string:uuid>', 'show_group', GroupController.show, methods=['GET'])

        apiv1.add_url_rule('/groups/<string:uuid>/add_user/<string:user_uuid>', 'add_user_to_group', GroupController.add_user, methods=['GET'])
        apiv1.add_url_rule('/groups/<string:uuid>/del_user/<string:user_uuid>', 'del_user_from_group',
                           GroupController.remove_user, methods=['GET'])

        apiv1.add_url_rule('/get_auth_token', 'get_auth_token', get_auth_token,methods=[ 'POST'])
        apiv1.add_url_rule('/register', 'register', register, methods=[ 'POST'])

        apiv1.add_url_rule('/feed', 'feed', FeedController.index, methods=['GET'])
        apiv1.add_url_rule('/feed', 'search_feed', FeedController.index, methods=['POST'])

        return apiv1