from functools import wraps
from flask import g
from flask_dance.contrib.github import make_github_blueprint, github
#from app import login_manager
from app.models.user import User, db
from flask import request, jsonify, redirect, url_for

from . import apiv1
import sys



github_blueprint = make_github_blueprint(
        client_id="ee944e4cffa32d553ace",
            client_secret="53ce9507ca2ce82419bcea36ec62f5c412c23fad",
    )



def get_auth_token():
    req_data = request.get_json()

    username = req_data['username']
    password = req_data['password']


    if username is None or username =="":
        return jsonify({"status": 400, "message": "no login params"})

    user = User.query.filter(User.username==username).first()
    if user is None or not user.check_password(password):

        return jsonify({"status":404, "message":"Invalid login"})

    auth_token = user.encode_auth_token(user.id)

    responseObject = {
        'status': 200,
        'message': 'Token Enclosed.',
        'auth_token': auth_token.decode()
    }
    return jsonify(responseObject)



def register():

    req_data = request.get_json()

    valid, valid_message = User.validate(req_data)
    if valid:
        user = User(username=req_data["username"], email=req_data["email"])
        user.set_password(req_data["password"])
        db.session.add(user)
        db.session.commit()
        user = User.query.filter(User.email==req_data["email"]).first()
        auth_token = user.encode_auth_token(user.id)
        return jsonify({"status":200, "message":"User Created", "token":auth_token.decode()})

    else:
        return jsonify({"status": 400, "message": valid_message})



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
              description: Image representing the news item

              '''
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])

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
            print(resp)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                if user:
                    a= True
                else:
                    a= False
        else:
            a=False

        if a == True:
            g.user = user
            return function_to_wrap(*args, **kwargs)
        else:
            return jsonify({"Status":401, "message":"Not authenticated"})

    return wrap