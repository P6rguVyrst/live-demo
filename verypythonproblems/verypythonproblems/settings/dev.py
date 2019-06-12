from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=us%c1odh3bobcemy^h#lo$d2srfc*q0zrs(-$xgpl-w_g6zf0'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
