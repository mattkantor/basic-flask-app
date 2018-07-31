from functools import wraps
from flask import g
from flask_dance.contrib.github import make_github_blueprint, github
#from app import login_manager
from app.models.user import User, db
from flask import request, jsonify, redirect, url_for

from app.schema.user_schema import user_schema
from . import apiv1
from .api_helper import  common_response
import sys



github_blueprint = make_github_blueprint(
        client_id="ee944e4cffa32d553ace",
            client_secret="53ce9507ca2ce82419bcea36ec62f5c412c23fad",
    )



def get_auth_token():
    req_data = request.get_json()

    #username = req_data['username']
    password = req_data['password']
    email = req_data["email"]


    if email is None or email =="":
        return common_response(status=404, message="No login parameters")

    user = User.query.filter(User.email==email).first()
    if user is None or not user.check_password(password):

        return common_response(status=401, message="Unauthorized")

    auth_token = user.encode_auth_token()
    g.user = user
    #g.value.token=auth_token.decode()

    return common_response(token=auth_token.decode())



def register():

    req_data = request.get_json(force=True)
    print("---------")
    print(req_data)

    print(req_data["email"])


    try:
        user = User( email=req_data["email"])
        user.set_password(req_data["password"])
        db.session.add(user)
        db.session.commit()
        db.session.flush()
        user = User.query.filter(User.email==req_data["email"]).first()
        auth_token = user.encode_auth_token()
        #g.value.token = auth_token.decode()
        g.user = user
        return common_response( message="User Created", object=user_schema.dumps(user),token=auth_token.decode())
    except AssertionError as message:
        db.session.rollback()
        return common_response(status=400, message=message, token="")




@github_blueprint.route("/github")
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
              description: Image representing the news item'''
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return common_response(status=200, message="You are @{login} on GitHub".format(login=resp.json()["login"]))


def login_required(function_to_wrap):
    @wraps(function_to_wrap)
    def wrap(*args, **kwargs):
        a = False
        auth_header = request.headers.get('Authorization')

        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = None
            a = False

        if auth_token:

            resp = User.decode_auth_token(auth_token)



            user = User.query.filter(User.uuid==resp).first()



            if user:
                a=True
                g.user = user

            else:
                a= False
        else:
            a=False

        if a == True:

            return function_to_wrap(*args, **kwargs)
        else:
            return common_response(status=401, message="Not authorized")


    return wrap