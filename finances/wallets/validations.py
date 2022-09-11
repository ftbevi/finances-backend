from django.core.exceptions import ValidationError


class TransactionValidations:
    @classmethod
    def validate_negative_amount(self, amount):
        if amount < 0:
            raise ValidationError(f"{self.amount} is not an monetary valid number")
