from flask import Blueprint, jsonify, request

from converter_app.converter.validator import Validator

conv = Blueprint('conv', __name__)

@conv.route('/api/convert', methods=['GET'])
def convert():
    from_currency = request.args.get('from', type=str, default=None)
    to_currency = request.args.get('to', type=str, default=None)
    amount = request.args.get('amount', type=int, default=None)
    return operate(from_currency, to_currency, amount)


def operate(from_currency: str, to_currency: str, amount: int or float):
    validator = Validator()
    validate = validator.validate_input(from_currency, to_currency, amount)
    if not validate:
        response = jsonify({"code:": 400, "name:": "wrong parameters type or length"})
        return response, 400
    return 'success', 200
