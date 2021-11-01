from flask import Blueprint, Response, json, jsonify
from werkzeug.exceptions import HTTPException

errors = Blueprint("error", __name__)


class ApiException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["code"] = self.status_code
        rv["message"] = self.message
        return rv


@errors.app_errorhandler(ApiException)
def handle_invalid_usage(error: ApiException) -> Response:
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@errors.app_errorhandler(HTTPException)
def handle_exception(error: HTTPException) -> Response:
    response = error.get_response()
    response.data = json.dumps({"code": error.code, "name": error.name, "description": error.description})
    response.content_type = "application/json"
    return response
