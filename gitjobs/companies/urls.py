from django.conf.urls import patterns,url
from django.conf.urls import patterns, url, include
from .models import Company
from . import views as company_views

urlpatterns = [
    url(r'^(?P<company_slug>[0-9A-Za-z\-]+)/$', company_views.CompanyDetails.as_view(), name='company_details'),
    url(r'^(?P<company_slug>[0-9A-Za-z\-]+)/edit$', company_views.CompanyEditView.as_view(), name='comapny_edit')
]
