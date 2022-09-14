from pytest_factoryboy import register

from .factories import CategoryFactory, TransactionFactory, UserFactory

register(UserFactory)
register(CategoryFactory)
register(TransactionFactory)
