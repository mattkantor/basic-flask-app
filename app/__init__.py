import os

from celery import Celery
from flask import Flask

from app.models.news import migrate, db
from app.api import apiv1
from .routes import Route
from flasgger import Swagger

from flask import Flask, redirect, url_for

from flask_dance.contrib.github import make_github_blueprint, github

from flask import jsonify

config_variable_name = 'FLASK_CONFIG_PATH'
default_config_path = os.path.join(os.path.dirname(__file__), '../config/local.py')
os.environ.setdefault(config_variable_name, default_config_path)

os.environ.setdefault("OAUTHLIB_INSECURE_TRANSPORT", "1")


def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)
    app.secret_key = "aldfkja;skdf"

    github_blueprint = make_github_blueprint(
        client_id="ee944e4cffa32d553ace",
        client_secret="53ce9507ca2ce82419bcea36ec62f5c412c23fad",
    )

    Swagger(app)

    api_routes = Route.build(apiv1)
    app.register_blueprint(api_routes, url_prefix='/api/v1')


    @github_blueprint.route("/")
    def index():
        ''' Login
        Call this api passing a user key
        ---

        responses:
          500:
            description: Login is broken
          200:
            description: Login works
            schema:
              id: Login
              properties:
                title:
                  type: string
                  description: The article name
                  default: None
                image:
                  type: base/64
                  description: Image representing the news item

                  '''
        if not github.authorized:
            return redirect(url_for("github.login"))
        resp = github.get("/user")
        assert resp.ok
        return "You are @{login} on GitHub".format(login=resp.json()["login"])

    app.register_blueprint(github_blueprint, url_prefix="/login")

    if config_file:
        app.config.from_pyfile(config_file)
    else:
        app.config.from_envvar(config_variable_name)

    if settings_override:
        app.config.update(settings_override)

    init_app(app)




    return app



def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)


    #api.init_app(app)


def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
