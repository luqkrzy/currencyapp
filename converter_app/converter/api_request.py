
class ApiRequest:

    def __init__(self,  base_currency: str, to_currency: str, amount: float):
        self._base_currency = base_currency
        self._to_currency = to_currency
        self._amount = amount
        self._exchange_rate = None

    @property
    def base_currency(self) -> str:
        return self._base_currency

    @property
    def to_currency(self) -> str:
        return self._to_currency

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def exchange_rate(self) -> float:
        return self._exchange_rate

    @base_currency.setter
    def base_currency(self, base_currency: str) -> None:
        self._base_currency = base_currency

    @to_currency.setter
    def to_currency(self, to_currency: str) -> None:
        self._to_currency = to_currency

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate: str) -> None:
        self._exchange_rate = exchange_rate

    @amount.setter
    def amount(self, amount: str) -> None:
        self._amount = amount





