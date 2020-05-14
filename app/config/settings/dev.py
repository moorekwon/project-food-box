from .base import *

# SECRETS = SECRETS_FULL['dev']

DEBUG = True
WSGI_APPLICATION = 'config.wsgi.dev.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

print("os.path.join(BASE_DIR, 'db.sqlite3') >> ", os.path.join(BASE_DIR, 'db.sqlite3'))

ALLOWED_HOSTS += []
INSTALLED_APPS += []
