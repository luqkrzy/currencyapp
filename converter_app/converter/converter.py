from flask import jsonify, abort, Response

from converter_app.converter.api_request import ApiRequest
from converter_app.converter.converter_context import ConverterContext
from converter_app.converter.converter_country_curr import ConverterBaseCountryCurrency
from converter_app.converter.converter_alternative_curr import ConverterAlternativeCurrency
from converter_app.converter.validator import Validator
from converter_app.conversion.conversion import Conversion, ConversionSchema


class Converter:
    _COUNTRY_CURRENCY = 'PLN'

    def __init__(self, validator: Validator):
        self.validator = validator

    def convert(self, api_request: ApiRequest) -> Response:
        validate = self.validator.validate_input(api_request)

        if not validate:
            abort(400)

        if api_request.base_currency.lower() == Converter._COUNTRY_CURRENCY.lower():
            context = ConverterContext(strategy=ConverterBaseCountryCurrency(), api_request=api_request)
        else:
            context = ConverterContext(strategy=ConverterAlternativeCurrency(), api_request=api_request)
        result = context.convert_currency()

        return self.__prepare_response(api_request, result)

    def __prepare_response(self, api_request: ApiRequest, result: float) -> Response:
        schema = ConversionSchema()
        conversion = Conversion(api_request.base_currency, api_request.to_currency, api_request.amount,
                                api_request.exchange_rate, result)
        resp = schema.dump(conversion)
        return jsonify(resp)
