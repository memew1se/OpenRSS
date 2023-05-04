from .base import *  # noqa

DEBUG = False

# TODO: change this in prod
ALLOWED_HOSTS = ("<hostname>",)

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 60 * 60
CACHE_MIDDLEWARE_KEY_PREFIX = ""

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",)
}
