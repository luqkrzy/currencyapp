import requests
from abc import ABC, abstractmethod
from converter_app.converter.api_request import ApiRequest


class ConverterStrategy(ABC):

    _TIME = "today"
    _RATE_FIELD = 'rates'
    _RATE_PRICE_FIELD = 'mid'
    _API_URL = "http://api.nbp.pl/api/exchangerates/rates/a"

    @abstractmethod
    def convert(self, api_request: ApiRequest) -> float:
        pass

    @abstractmethod
    def compute(self, amount: float, exchange_rate: float) -> float:
        pass

    def get_exchange_rate_from_api(self, currency: str) -> float:
        req = requests.get(f"{ConverterStrategy._API_URL}/{currency}/{ConverterStrategy._TIME}")
        rate = None
        if req.status_code == 200:
            json = req.json()
            try:
                rate = json[ConverterStrategy._RATE_FIELD][0][ConverterStrategy._RATE_PRICE_FIELD]
            except KeyError:
                pass
        return rate
