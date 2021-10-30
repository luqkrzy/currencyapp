import requests
from datetime import date
from flask import Response, abort, jsonify

from converter_app.conversion.conversion import Conversion, ConversionSchema
from converter_app.converter.validator import Validator
from settings import COUNTRY_CURRENCY_PLN, NBP_API_URL
from converter_app import db
from model.rate import Rate


class Converter:
    def __init__(self, validator: Validator):
        self.validator = validator

    def convert(self, base_currency: str, to_currency: str, amount: float) -> Response:
        validate = self.validator.validate_input(base_currency=base_currency, to_currency=to_currency, amount=amount)
        if not validate:
            abort(400)
        to_curr_ex_rate = self.get_exchange_rate_from_api(to_currency)
        result = amount / to_curr_ex_rate
        if base_currency.upper() != COUNTRY_CURRENCY_PLN:
            base_curr_ex_rate = self.get_exchange_rate_from_api(currency=base_currency)
            result = result * base_curr_ex_rate
        return self.prepare_response(
            base_currency=base_currency,
            to_currency=to_currency,
            amount=amount,
            result=result,
            exchange_rate=to_curr_ex_rate,
        )

    def get_exchange_rate_from_api(self, currency: str) -> float:
        today = date.today().strftime("%Y-%m-%d")
        data = Rate.query.filter(Rate.code == currency.upper() and Rate.date == today).first()
        if data:
            return data.value
        req = requests.get(f"{NBP_API_URL}/{currency}")
        value = None
        if req.status_code == 200:
            response_data = req.json()
            try:
                value = response_data["rates"][0]["mid"]
                rate = Rate(code=currency, date=today, value=value)
                db.session.add(rate)
                db.session.commit()
            except KeyError:
                abort(400)
        elif req.status_code == 404:
            abort(404)
        return value

    def prepare_response(
        self, base_currency: str, to_currency: str, amount: float, result: float, exchange_rate: float
    ) -> Response:
        schema = ConversionSchema()
        conversion = Conversion(
            base_currency=base_currency.upper(),
            to_currency=to_currency.upper(),
            amount=amount,
            exchange_rate=exchange_rate,
            result=round(result, 4),
        )
        resp = schema.dump(conversion)
        return jsonify(resp)
