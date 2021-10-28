from converter_app.converter.api_request import ApiRequest

class Validator:

    _CODE_LEN = 3

    def validate_input(self, api_request: ApiRequest) -> bool:
        return all([self.__validate_currency(api_request.base_currency),
                    self.__validate_currency(api_request.to_currency), isinstance(api_request.amount, (int, float))])

    def __validate_currency(self, currency: str) -> bool:
        return isinstance(currency, str) and len(currency) == Validator._CODE_LEN
