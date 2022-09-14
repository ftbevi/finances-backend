import random

import pytest
from django.core.exceptions import ValidationError
from django.db.models import Sum
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


def test_transaction_balance(db, user_factory, transaction_factory):
    user = user_factory.create()

    # creating randomic invoices and revenues
    quantity_transactions = random.randrange(1, 10)
    for _ in range(quantity_transactions):
        _ = transaction_factory(owner=user, transaction_type=TransactionType.INVOICE)

    quantity_transactions = random.randrange(1, 10)
    for _ in range(quantity_transactions):
        _ = transaction_factory(owner=user, transaction_type=TransactionType.REVENUE)

    # get invoices and revenues
    invoices = (
        Transaction.objects.filter(owner=user, transaction_type=TransactionType.INVOICE)
        .aggregate(invoices_totals=Sum("amount"))
        .get("invoices_totals")
    )
    revenue = (
        Transaction.objects.filter(owner=user, transaction_type=TransactionType.REVENUE)
        .aggregate(revenue_totals=Sum("amount"))
        .get("revenue_totals")
    )

    balance = revenue - invoices
    transaction_balance = Transaction.balance(user)

    assert invoices == transaction_balance["invoices"]
    assert revenue == transaction_balance["revenue"]
    assert balance == transaction_balance["balance"]
