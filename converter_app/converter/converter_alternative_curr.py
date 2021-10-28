from flask import abort
from converter_app.converter.api_request import ApiRequest
from converter_app.converter.converter_strategy import ConverterStrategy

class ConverterAlternativeCurrency(ConverterStrategy):

    def convert(self, api_request: ApiRequest) -> float:
        base_curr_ex_rate = self.get_exchange_rate_from_api(api_request.base_currency)
        to_curr_ex_rate = self.get_exchange_rate_from_api(api_request.to_currency)
        if base_curr_ex_rate == None or to_curr_ex_rate == None:
            abort(400)
        exchange_rate = base_curr_ex_rate/to_curr_ex_rate

        api_request.exchange_rate = exchange_rate
        return self.compute(api_request.amount, exchange_rate)

    def compute(self, amount: float, exchange_rate: float) -> float:
        return amount*exchange_rate
