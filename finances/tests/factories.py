import random

import factory
from faker import Faker

from finances.accounts.models import User
from finances.wallets.models import Category, Transaction

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = faker.email()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    owner = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    amount = random.randrange(1, 1000)
    title = faker.name()
