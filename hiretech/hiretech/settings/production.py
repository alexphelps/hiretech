from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

EMAIL_BASE_URL = 'http://52.4.190.205:8080/'

ALLOWED_HOSTS = [
    '*'
]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME',''),
            'USER': os.environ.get('DB_USER',''),
            'PASSWORD': os.environ.get('DB_PASSWORD',''),
            'HOST': os.environ.get('DB_HOST',''),
            'PORT': '',
        }
    }
