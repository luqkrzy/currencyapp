from converter_app.converter.converter_strategy import ConverterStrategy
from converter_app.converter.api_request import ApiRequest

class ConverterContext:

    def __init__(self, strategy: ConverterStrategy, api_request: ApiRequest):
        self.strategy = strategy
        self.api_request = api_request

    def convert_currency(self) -> float:
        return self.strategy.convert(self.api_request)

