from flask import abort
from converter_app.converter.api_request import ApiRequest
from converter_app.converter.converter_strategy import ConverterStrategy

class ConverterBaseCountryCurrency(ConverterStrategy):

    def convert(self, api_request: ApiRequest) -> float:
        exchange_rate = self.get_exchange_rate_from_api(api_request.to_currency)
        if exchange_rate == None:
            abort(400)
        api_request.exchange_rate = exchange_rate
        return self.compute(api_request.amount, exchange_rate)

    def compute(self, amount: float, exchange_rate: float) -> float:
        return amount/exchange_rate
