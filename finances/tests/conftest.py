# import os
# import pytest
# from django.conf import settings

from pytest_factoryboy import register

from .factories import CategoryFactory, UserFactory

register(UserFactory)
register(CategoryFactory)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'finances.settings'


# @pytest.fixture(scope='session')
# def pytest_configure():
#     settings.DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': ':memory:',
#         }
#     }
