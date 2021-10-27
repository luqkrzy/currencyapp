import requests
from flask import jsonify, abort, Response

from converter_app.converter.validator import Validator
from converter_app.model.conversion import Conversion, ConversionSchema
from converter_app.converter.api_request import ApiRequest


class Converter:

    _COUNTRY_CURRENCY = 'PLN'
    _TIME = "today"
    _RATE_FIELD = 'rates'
    _RATE_PRICE_FIELD = 'mid'
    _API_URL = "http://api.nbp.pl/api/exchangerates/rates/a"

    def __init__(self):
        self.validator = Validator()

    def convert(self, api_request: ApiRequest) -> Response:
        validate = self.validator.validate_input(api_request)

        if not validate:
            abort(400)

        exchange_rate = self.__get_rate(api_request)
        if exchange_rate == None:
            abort(400)

        result = self.__convert_currency(api_request.amount, exchange_rate)
        resp = self.__prepare_response(api_request, exchange_rate, result)
        return jsonify(resp)

    def __get_rate(self, api_request: ApiRequest) -> float:
        exchange_rate = None

        if api_request.base_currency.lower() == Converter._COUNTRY_CURRENCY.lower():
            exchange_rate = self.__get_exchange_rate_from_api(api_request.to_currency)
        elif api_request.base_currency.lower() != Converter._COUNTRY_CURRENCY.lower():
            exchange_rate = self.__get_exchange_rate_from_api(api_request.base_currency)

        return exchange_rate

    def __get_exchange_rate_from_api(self, to_currency: str) -> float:
        req = requests.get(f"{Converter._API_URL}/{to_currency}/{Converter._TIME}")
        rate = None
        if req.status_code == 200:
            json = req.json()
            try:
                rate = json[Converter._RATE_FIELD][0][Converter._RATE_PRICE_FIELD]
            except KeyError:
                pass
        return rate

    def __prepare_response(self, api_request: ApiRequest, exchange_rate: float, result: float) -> Response:
        schema = ConversionSchema()
        conversion = Conversion(api_request.base_currency, api_request.to_currency, api_request.amount, exchange_rate, result)
        resp = schema.dump(conversion)
        return resp

    def __convert_currency(self, amount, exchange_rate) -> float:
        return amount/exchange_rate

