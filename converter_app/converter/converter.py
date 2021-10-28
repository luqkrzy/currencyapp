import requests
from flask import Response, abort, jsonify

from converter_app.conversion.conversion import Conversion, ConversionSchema
from converter_app.converter.api_request import ApiRequest
from converter_app.converter.validator import Validator


class Converter:
    _COUNTRY_CURRENCY_PLN = "PLN"
    _TIME = "today"
    _RATE_FIELD = "rates"
    _RATE_PRICE_FIELD = "mid"
    _API_URL = "http://api.nbp.pl/api/exchangerates/rates/a"

    def __init__(self, validator: Validator):
        self.validator = validator

    def convert(self, api_request: ApiRequest) -> Response:
        validate = self.validator.validate_input(api_request=api_request)

        if not validate:
            abort(400)

        to_curr_ex_rate = self.get_exchange_rate_from_api(currency=api_request.to_currency)
        api_request.exchange_rate = to_curr_ex_rate
        result = api_request.amount / to_curr_ex_rate

        if api_request.base_currency.lower() != Converter._COUNTRY_CURRENCY_PLN.lower():
            base_curr_ex_rate = self.get_exchange_rate_from_api(currency=api_request.base_currency)
            result = result * base_curr_ex_rate

        return self.prepare_response(api_request=api_request, result=result)

    def get_exchange_rate_from_api(self, currency: str) -> float:
        req = requests.get(f"{Converter._API_URL}/{currency}/{Converter._TIME}")
        rate = None
        if req.status_code == 200:
            json = req.json()
            try:
                rate = json[Converter._RATE_FIELD][0][Converter._RATE_PRICE_FIELD]
            except KeyError:
                abort(400)
        return rate

    def prepare_response(self, api_request: ApiRequest, result: float) -> Response:
        schema = ConversionSchema()
        conversion = Conversion(
            base_currency=api_request.base_currency,
            to_currency=api_request.to_currency,
            amount=api_request.amount,
            exchange_rate=api_request.exchange_rate,
            result=result,
        )
        resp = schema.dump(conversion)
        return jsonify(resp)
