from .base import *  # noqa: F403, F401

STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), "statics")  # noqa: F405
STATIC_URL = "/statics/"
MEDIA_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), "media")  # noqa: F405
MEDIA_URL = "/media/"
