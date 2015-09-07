from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Google Recaptcha
os.environ['NORECAPTCHA_TESTING'] = 'True'
