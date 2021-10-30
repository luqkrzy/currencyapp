import requests
from flask import Response, abort, jsonify

from converter_app.conversion.conversion import Conversion, ConversionSchema
from converter_app.converter.api_request import ApiRequest
from converter_app.converter.validator import Validator
from settings import NBP_API_URL, COUNTRY_CURRENCY_PLN

class Converter:

    def __init__(self, validator: Validator):
        self.validator = validator

    def convert(self, api_request: ApiRequest) -> Response:
        validate = self.validator.validate_input(api_request=api_request)
        if not validate:
            abort(400)
        to_curr_ex_rate = self.get_exchange_rate_from_api(currency=api_request.to_currency)
        api_request.exchange_rate = to_curr_ex_rate
        result = api_request.amount / to_curr_ex_rate
        if api_request.base_currency.upper() != COUNTRY_CURRENCY_PLN:
            base_curr_ex_rate = self.get_exchange_rate_from_api(currency=api_request.base_currency)
            result = result * base_curr_ex_rate
        return self.prepare_response(api_request=api_request, result=result)

    def get_exchange_rate_from_api(self, currency: str) -> float:
        req = requests.get(f'{NBP_API_URL}/{currency}')
        rate = None
        if req.status_code == 200:
            response_data = req.json()
            try:
                rate = response_data['rates'][0]['mid']
            except KeyError:
                abort(400)
        elif req.status_code == 404:
            abort(404)
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
