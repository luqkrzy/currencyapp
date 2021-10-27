

class ApiRequest:

    def __init__(self,  base_currency: str, to_currency: str, amount: int or float):
        self.base_currency = base_currency
        self.to_currency = to_currency
        self.amount = amount
