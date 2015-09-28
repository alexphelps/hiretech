from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Email Errors 
ADMINS = (
    ('HireTech Errors', 'errors@hiretech.io'),
)

EMAIL_BASE_URL = 'http://hiretech.io'

ALLOWED_HOSTS = [
    'hiretech.io'
]

#MEDIA_URL = '//d39h1855s3pz3w.cloudfront.net/media/'
#STATIC_URL = '//d39h1855s3pz3w.cloudfront.net/static/'

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
