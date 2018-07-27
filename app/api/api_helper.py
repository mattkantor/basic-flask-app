from flask import  jsonify


def common_response(status=200, message="OK", object={}, token=""):

        #token = g.token
    return jsonify({"status":status,"message":message, "data":object,"token":token })

