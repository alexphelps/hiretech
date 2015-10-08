from django.conf import settings
from users.models import UserProfile

def production(request):
    return {
        'production': settings.PRODUCTION
    }
