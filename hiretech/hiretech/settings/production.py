from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Haystack
HAYSTACK_SIGNAL_PROCESSOR = 'search.signals.RealtimeSignalProcessor'

EMAIL_BASE_URL = 'http://hiretech.io/'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'DB_NAME',
            'USER': 'DB_USER',
            'PASSWORD': 'DB_PASSWORD',
            'HOST': 'DB_HOST',
            'PORT': 'DB_PORT',
        }
    }
