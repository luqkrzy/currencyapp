from flask import Blueprint, json

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def handle_exception(error):
    response = error.get_response()
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    response.content_type = "application/json"
    return response


@errors.app_errorhandler(400)
def handle_exception(error):
    response = error.get_response()
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": "wrong parameter type or length",
    })
    response.content_type = "application/json"
    return response
