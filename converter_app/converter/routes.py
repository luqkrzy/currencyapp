from flask import Blueprint, jsonify, request

conv = Blueprint('conv', __name__)


@conv.route('/api/convert', methods=['GET'])
def convert():
    from_currency = request.args.get('from', type=str, default=None)
    to_currency = request.args.get('to', type=str, default=None)
    amount = request.args.get('amount', type=int, default=None)
    print(from_currency, to_currency, type(amount))

    return 'success', 200
