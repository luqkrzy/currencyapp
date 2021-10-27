from flask import Blueprint, request, abort

from converter_app.converter.validator import Validator

conv = Blueprint('conv', __name__)

@conv.route('/api/convert', methods=['GET'])
def convert():
    from_currency = request.args.get('from', type=str, default=None)
    to_currency = request.args.get('to', type=str, default=None)
    amount = request.args.get('amount', type=float, default=None)
    return operate(from_currency, to_currency, amount)


def operate(from_currency: str, to_currency: str, amount: int or float):
    validator = Validator()
    validate = validator.validate_input(from_currency, to_currency, amount)
    if not validate:
        abort(400)
    return 'success', 200
