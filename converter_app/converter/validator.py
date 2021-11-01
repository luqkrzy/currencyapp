class Validator:
    def validate_input(self, base_currency: str, to_currency: str, amount: float) -> bool:
        return all(
            [
                self._validate_currency(currency=base_currency),
                self._validate_currency(currency=to_currency),
                isinstance(amount, (int, float)) and amount > 0,
            ]
        )

    def _validate_currency(self, currency: str) -> bool:
        return isinstance(currency, str) and len(currency) == 3
