from .base import *

SECRETS = SECRETS_FULL['production']

DEBUG = False
WSGI_APPLICATION = 'config.wsgi.production.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = SECRETS['DATABASES']

ALLOWED_HOSTS += [
    '*'
]

INSTALLED_APPS += []
