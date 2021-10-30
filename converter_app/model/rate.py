from converter_app import db


class Rate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Rate('{self.id}, {self.code}, {self.date}, {self.value}"
