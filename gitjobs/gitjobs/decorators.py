from functools import wraps
from django.shortcuts import get_object_or_404,render
from django.core.exceptions import PermissionDenied
from users.models import UserProfile
from companies.models import Company

def userincompany(func):
    def wrapper(request, *args, **kwargs):
        company_slug = kwargs['company_slug']
        current_user = request.request.user
        current_user_id = current_user.id
        current_user_profile = UserProfile.objects.get(user__id=current_user_id)
        company = get_object_or_404(Company, company_slug=company_slug)
        current_user_company = current_user_profile.company
        if current_user_company != company:
            raise PermissionDenied
        else:
            kwargs['company'] = company
            kwargs['current_user_company'] = current_user_company
            return func(request,*args,**kwargs)
    return wrapper
