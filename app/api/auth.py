from flask_dance.contrib.github import make_github_blueprint, github

github_blueprint = make_github_blueprint(
        client_id="ee944e4cffa32d553ace",
        client_secret="53ce9507ca2ce82419bcea36ec62f5c412c23fad",
    )


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

