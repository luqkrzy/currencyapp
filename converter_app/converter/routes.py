from flask import Blueprint, request

from converter_app.converter.converter import Converter
from converter_app.converter.validator import Validator
from converter_app.error.error import ApiException

conv = Blueprint("conv", __name__)


@conv.route("/api/convert", methods=["GET"])
def convert():
    base_currency = request.args.get("from", type=str)
    to_currency = request.args.get("to", type=str)
    amount = request.args.get("amount", type=float)
    if base_currency is None or to_currency is None or amount is None:
        raise ApiException('Insufficient parameters')
    converter = Converter(validator=Validator())
    resp = converter.convert(base_currency=base_currency.upper(), to_currency=to_currency.upper(), amount=amount)
    return resp
