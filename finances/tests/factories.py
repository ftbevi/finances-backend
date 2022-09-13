import factory
from faker import Faker

from finances.accounts.models import User
from finances.wallets.models import Category

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = faker.email()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
