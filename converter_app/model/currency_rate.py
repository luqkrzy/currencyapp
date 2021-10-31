from converter_app import db


class CurrencyRate(db.Model):
    date = db.Column(db.Date(), nullable=False, primary_key=True)
    currency_code = db.Column(db.String(3), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Rate('{self.id}, {self.code}, {self.date}, {self.value}"
