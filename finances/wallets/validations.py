from django.core.exceptions import ValidationError


class TransactionValidations:
    @classmethod
    def validate_negative_amount(cls, amount):
        if amount < 0:
            raise ValidationError(f"{amount} is not an monetary valid number")
        return True
