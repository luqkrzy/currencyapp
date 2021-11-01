from converter_app import db


class CurrencyRate(db.Model):
    def __init__(self, date, currency_code, value):
        self.value = value
        self.currency_code = currency_code
        self.date = date

    date = db.Column(db.Date(), nullable=False, primary_key=True)
    currency_code = db.Column(db.String(3), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Rate({self.currency_code}, {self.date}, {self.value})"
