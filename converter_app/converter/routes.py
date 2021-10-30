from flask import Blueprint, request

from converter_app.converter.converter import Converter
from converter_app.converter.validator import Validator

conv = Blueprint("conv", __name__)


@conv.route("/api/convert", methods=["GET"])
def convert():
    base_currency = request.args.get("from", type=str, default=None)
    to_currency = request.args.get("to", type=str, default=None)
    amount = request.args.get("amount", type=float, default=None)
    converter = Converter(validator=Validator())
    resp = converter.convert(base_currency=base_currency.upper(), to_currency=to_currency.upper(), amount=amount)
    return resp
