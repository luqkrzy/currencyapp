from flask import Blueprint, json, Response
from werkzeug.exceptions import HTTPException

errors = Blueprint("error", __name__)


def base_handle_exception(error: HTTPException) -> Response:
    response = error.get_response()
    response.data = json.dumps({"code": error.code, "name": error.name, "description": error.description})
    response.content_type = "application/json"
    return response


@errors.app_errorhandler(HTTPException)
def handle_exception(error: HTTPException) -> Response:
    response = base_handle_exception(error)
    return response


@errors.app_errorhandler(400)
def handle_exception(error: HTTPException):
    response = error.get_response()
    response.data = json.dumps(
        {"code": error.code, "name": error.name, "description": "wrong parameter type or length"}
    )
    response.content_type = "application/json"
    return response
