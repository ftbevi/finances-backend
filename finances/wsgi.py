import os

from django.core.wsgi import get_wsgi_application

PROJECT_ENVIRONMENT = os.environ.get("PROJECT_ENVIRONMENT", "local")

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"finances.settings.{PROJECT_ENVIRONMENT}"
)

application = get_wsgi_application()
