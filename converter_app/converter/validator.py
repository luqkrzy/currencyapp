
class Validator:

    _code_len = 3

    def validate_input(self, from_currency: str, to_currency: str, amount: int or float) -> bool:
        return all([self.__validate_currency(from_currency), self.__validate_currency(to_currency), isinstance(amount, (int, float))])

    def __validate_currency(self, currency: str) -> bool:
        return isinstance(currency, str) and len(currency) == Validator._code_len
