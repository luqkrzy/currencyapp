from converter_app.converter.converter_strategy import ConverterStrategy
from converter_app.converter.api_request import ApiRequest

class ConverterContext:

    def __init__(self, strategy: ConverterStrategy, api_request: ApiRequest):
        self._strategy = strategy
        self._api_request = api_request

    @property
    def api_request(self) -> ApiRequest:
        return self._api_request

    @property
    def strategy(self) -> ConverterStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ConverterStrategy) -> None:
        self._strategy = strategy


    def convert_currency(self) -> float:
        return self._strategy.convert(self._api_request)





