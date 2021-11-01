from unittest import TestCase
from converter_app.converter.validator import Validator


class TestValidator(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.validator = Validator()

    @classmethod
    def tearDownClass(cls):
        cls.validator = None

    def test_validate_input_correct(self):
        self.assertTrue(self.validator.validate_input('pln', 'Usd', 11.5))

    def test_validate_input_wrong_length(self):
        self.assertFalse(self.validator.validate_input('plnx', 'Usd', 111.58))

    def test_validate_input_wrong_amount_type(self):
        self.assertFalse(self.validator.validate_input('pln', 'Usd', '10.45'))


