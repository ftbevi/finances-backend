import pytest
from django.core.exceptions import ValidationError

from finances.wallets.validations import TransactionValidations


def test_negative_values_success():
    valid = TransactionValidations.validate_negative_amount(amount=10)
    assert valid is True


def test_negative_values_error():
    amount = -20
    error_message = f"['{amount} is not an monetary valid number']"
    with pytest.raises(ValidationError) as ex:
        TransactionValidations.validate_negative_amount(amount=amount)
    assert error_message == str(ex.value)
