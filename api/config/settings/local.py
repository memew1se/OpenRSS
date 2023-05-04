from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["*"]

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 5
CACHE_MIDDLEWARE_KEY_PREFIX = ""

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        # "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework.renderers.JSONRenderer",
    )
}
