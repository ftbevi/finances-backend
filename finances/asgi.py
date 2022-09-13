import os

from django.core.asgi import get_asgi_application

PROJECT_ENVIRONMENT = os.environ.get("PROJECT_ENVIRONMENT", "local")

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"finances.settings.{PROJECT_ENVIRONMENT}"
)

application = get_asgi_application()
