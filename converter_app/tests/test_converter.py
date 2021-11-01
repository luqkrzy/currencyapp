from unittest import TestCase, mock

from converter_app.converter.validator import Validator
from converter_app.converter.converter import Converter
from model.currency_rate import CurrencyRate

class ResponseMock:
    status_code = 400


class TestConverter(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.converter = Converter(Validator())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.converter = None

    @mock.patch(
        "converter_app.converter.converter.Converter.get_currency_rate_from_db",
        return_value=CurrencyRate("USD", "2021-11-01", 3.999))
    def test_get_exchange_rate_from_api_rate_found_in_db(self, rate):
        result = self.converter.get_exchange_rate_from_api("USD")
        self.assertEqual(3.999, result)

    @mock.patch(
        "converter_app.converter.converter.Converter.get_exchange_rate_from_api",
        return_value=3.9664)
    def test_convert(self, exchange_rate):
        result = self.converter.convert('PLN', 'USD', 10)
        self.assertEqual(2.5212, result.get_json()['result'])

    @mock.patch(
        "converter_app.converter.converter.Converter.get_currency_rate_from_db",
        return_value=None)
    @mock.patch(
        "converter_app.converter.converter.requests.get",
        return_value=ResponseMock())
    def test_get_exchange_rate_from_api_bad_nbp_response(self, rate, kaczka):
        result = self.converter.get_exchange_rate_from_api("USD")


