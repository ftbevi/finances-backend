import pytest
from django.core.exceptions import ValidationError
from faker import Faker

from finances.wallets.models import Transaction, TransactionType

faker = Faker()


def test_create_transation_success(db, user_factory, category_factory):
    user = user_factory.create()
    category = category_factory.create()
    data = {
        "owner": user,
        "category": category,
        "title": faker.name(),
        "transaction_type": TransactionType.INVOICE,
        "amount": 100,
    }
    transaction = Transaction.objects.create(**data)

    assert data["title"] == transaction.title
    assert data["amount"] == transaction.amount
    assert user.username == transaction.owner.username
    assert category.title == transaction.category.title
    assert TransactionType.INVOICE == transaction.transaction_type


def test_create_transation_error_negative_value(db, user_factory, category_factory):
    user = user_factory.create()
    category = category_factory.create()
    amount = -100
    data = {
        "owner": user,
        "category": category,
        "title": faker.name(),
        "transaction_type": TransactionType.INVOICE,
        "amount": amount,
    }
    error_message = f"['{amount} is not an monetary valid number']"
    with pytest.raises(ValidationError) as ex:
        _ = Transaction.objects.create(**data)
    assert error_message == str(ex.value)
