from marshmallow import Schema, fields


class Conversion:
    def __init__(self, base_currency: str, to_currency: str, amount: float, exchange_rate: float, result: float):
        self.base_currency = base_currency
        self.to_currency = to_currency
        self.amount = amount
        self.exchange_rate = exchange_rate
        self.result = result

    def __repr__(self):
        return (
            f"Conversion(base_currency='{self.base_currency}', to_currency='{self.to_currency}, "
            f"amount='{self.amount}', result='{self.result}')"
        )


class ConversionSchema(Schema):
    base_currency = fields.Str()
    to_currency = fields.Str()
    amount = fields.Float()
    exchange_rate = fields.Float()
    result = fields.Float()
