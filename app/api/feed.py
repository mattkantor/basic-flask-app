from flask import request, jsonify, g
from . import apiv1
from ..models.feed import Feed
from app import db
from .auth import login_required
from ..schema.news_schema import *
from .api_helper import *
from feedgen.feed import FeedGenerator
from flask import make_response

class FeedController():
    @staticmethod
    def rss():
        fg = FeedGenerator()
        fg.id('http://dogear-2112.herokapp.com')

        fg.title('Dogear Newsfeed')
        fg.author({'name': 'Haley Cohen', 'email': 'haley@dogearnews.com'})
        fg.link(href='http://dogearnews.com', rel='alternate')
        fg.logo('https://www.fixpocket.com/public_assets/uploads/beats/1523422664maxresdefault.jpg')

        fg.subtitle('The Dogear Social Newsfeed')
        fg.link(href='http://localhost:5000/rss/index.rss', rel='self')
        fg.language('en')

        news = News.query.order_by("created_at desc").limit(25).all()
        for n in news:

            fe = fg.add_entry()
            fe.id(n.url)
            fe.title(n.title)
            fe.link(href=n.url)
            fe.enclosure(n.picture_url, 0, 'image/jpeg')

            #fe.pubDate(n.created_at)

        rssfeed = fg.rss_str(pretty=True)

        response = make_response(rssfeed)
        response.headers['Content-Type'] = 'application/rss+xml'
        return response


    def __init__(self):
        ''''''

    @staticmethod
    @login_required
    def index():
        '''Returns all the news for a user
        Call this api passing a user key
        ---

        responses:
          500:
            description: Error The language is not awesome!
          200:
            description: A language with its awesomeness
            schema:
              id: News
              properties:
                title:
                  type: string
                  description: The article name
                  default: None
                image:
                  type: base/64
                  description: Image representing the news item

                  '''

        feed = db.session.query(Feed).all()
        return common_response(object=newses_schema.dump(feed))



    @staticmethod
    @login_required
    def search():
        '''Create a news for a user
                Call this api passing a user key
                ---

                responses:
                  500:
                    description: Meh, we're broken!
                  200:
                    description: News created!
                    schema:
                      id: awesome
                      properties:
                        title:
                          type: string
                          description: The article name
                          default: None
                        image:
                          type: base/64
                          description: Image representing the news item

                          '''

        req_data = request.get_json()

        news = Feed.search(q=req_data["q"], user_id=g.user.id)

        return common_response(object=newses_schema.dump(news))



