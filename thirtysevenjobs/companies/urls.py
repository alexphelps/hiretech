from django.conf.urls import patterns,url
from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from .models import Company
from . import views as company_views

urlpatterns = [
    url(r'^(?P<company_id>[0-9]+)/$', company_views.CompanyDetails.as_view(), name='company_details'),
    url(r'^(?P<company_id>[0-9]+)/edit$', company_views.CompanyEditView.as_view(), name='comapny_edit')
]
