from flask_dance.contrib.github import make_github_blueprint, github
#from app import login_manager
from app.models.user import User, db
from flask import request, jsonify, redirect, url_for
from flask_login import current_user, login_user, logout_user, LoginManager
from . import apiv1


github_blueprint = make_github_blueprint(
        client_id="ee944e4cffa32d553ace",
            client_secret="53ce9507ca2ce82419bcea36ec62f5c412c23fad",
    )


def login():
    if current_user.is_authenticated:
        return jsonify({"status":200, "message":"OK"})


    req_data = request.get_json()

    username = req_data['username']
    password = req_data['password']

    if username is None or username =="":
        return jsonify({"status": 400, "message": "no login params"})

    user = User.query.filter(User.username==username).first()
    if user is None or not user.check_password(password):

        return jsonify({"status":404, "message":"Invalid login"})
    #return jsonify({"status": 200, "message": "3"})
    login_user(user, remember=True)
    return jsonify({"status": 200, "message": "OK"})



def register():
    if current_user.is_authenticated:
        return jsonify({"status":201, "message":"Already logged in"})
    req_data = request.get_json()
    valid, valid_message = User.validate(req_data)
    if valid:
        user = User(username=req_data["username"], email=req_data["email"])
        user.set_password(req_data["password"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"status":200, "message":"User Created"})

    else:
        return jsonify({"status": 400, "message": valid_message})

@apiv1.route('/logout')
def logout():
    logout_user()
    return  jsonify({"status": 200, "message": "OK"})

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

