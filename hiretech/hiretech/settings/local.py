from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=xno-dxwgo+jv$$u=7&x^wav$wmsynl6-^!k!fs=$^7to_1t8='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Google Recaptcha
os.environ['NORECAPTCHA_TESTING'] = 'True'