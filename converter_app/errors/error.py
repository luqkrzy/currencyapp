from flask import Blueprint, json
from werkzeug.exceptions import HTTPException

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(HTTPException)
def handle_exception(error):
    response = error.get_response()
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    response.content_type = "application/json"
    return response
