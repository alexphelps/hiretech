from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Haystack
HAYSTACK_SIGNAL_PROCESSOR = 'search.signals.RealtimeSignalProcessor'
