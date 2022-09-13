import django_heroku

from .base import *  # noqa: F403, F401

# activate django-heroku.
django_heroku.settings(locals())

# database in heroku
db_from_env = dj_database_url.config(conn_max_age=600)  # noqa: F405
DATABASES["default"].update(db_from_env)  # noqa: F405

# static and media files in heroku
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # noqa: F405
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # noqa: F405
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
