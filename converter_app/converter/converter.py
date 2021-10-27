from flask import jsonify, abort, Response
from requests import request

from converter_app.converter.validator import Validator
from converter_app.model.conversion import Conversion, ConversionSchema
from converter_app.converter.api_request import ApiRequest


class Converter:

    _COUNTRY_CURRENCY = 'PLN'
    _API_URL = "http://api.nbp.pl/api/exchangerates/rates/a/"

    def __init__(self):
        self.validator = Validator()

    def convert(self, api_request: ApiRequest) -> Response:
        validate = self.validator.validate_input(api_request)
        if not validate:
            abort(400)

        exchange_rate = self.__get_rate(api_request)
        result = 10.78

        resp = self.__prepare_response(api_request, exchange_rate, result)
        return jsonify(resp)

    def __get_rate(self, api_request: ApiRequest) -> float:
        exchange_rate = None
        if api_request.base_currency.lower() == Converter._COUNTRY_CURRENCY.lower():
            exchange_rate = self.__get_exchange_rate_from_api(api_request.to_currency)
        return exchange_rate

    def __get_exchange_rate_from_api(self, to_currency: str) -> float:
        pass

    def __prepare_response(self, api_request: ApiRequest, exchange_rate: float, result: float) -> Response:
        schema = ConversionSchema()
        conversion = Conversion(api_request.base_currency, api_request.to_currency, api_request.amount, exchange_rate, result)
        resp = schema.dump(conversion)
        return resp
