from flask import Blueprint, request

from converter_app.converter.converter import Converter
from converter_app.converter.api_request import ApiRequest

conv = Blueprint('conv', __name__)

COUNTRY_CURRENCY = 'PLN'

@conv.route('/api/convert', methods=['GET'])
def convert():
    base_currency = request.args.get('from', type=str, default=None)
    to_currency = request.args.get('to', type=str, default=None)
    amount = request.args.get('amount', type=float, default=None)
    api_request = ApiRequest(base_currency, to_currency, amount)
    converter = Converter()
    resp = converter.convert(api_request)
    return resp

