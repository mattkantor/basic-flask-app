import flask
from flask import  jsonify


def common_response(status=200, message="OK", object={}, token=""):

    resp= flask.make_response(
            flask.jsonify({"status":status,"message":message, "data":object,"token":token }), status)

    return resp


