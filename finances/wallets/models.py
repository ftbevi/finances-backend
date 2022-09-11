from django.db import models

from finances.accounts.models import BaseModel, User

from .validations import TransactionValidations


class TransactionType:
    INVOICE = "invoice"
    REVENUE = "revenue"

    TRANSACTION_CHOICES = [
        (INVOICE, "invoice"),
        (REVENUE, "revenue"),
    ]


class Category(BaseModel):
    title = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.title}"


class Transaction(BaseModel):
    owner = models.ForeignKey(User, verbose_name="owner", on_delete=models.PROTECT)
    title = models.TextField()
    transaction_type = models.CharField(
        verbose_name="type",
        max_length=12,
        choices=TransactionType.TRANSACTION_CHOICES,
        default=TransactionType.INVOICE,
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="category",
        on_delete=models.PROTECT,
        related_name="transaction",
    )
    amount = models.DecimalField(verbose_name="amount", max_digits=11, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        TransactionValidations.validate_negative_amount(self.amount)
        super().save(*args, **kwargs)
