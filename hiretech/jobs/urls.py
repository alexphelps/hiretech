from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from companies.models import Company
from . import views as job_views


urlpatterns = [
    url(r'^$', job_views.JobIndex.as_view(), name='jobindex'),
    url(r'^(?P<company_slug>[0-9A-Za-z\-]+)/add/$', login_required(job_views.JobAddNew.as_view()), name='jobadd'),
    url(r'^(?P<job_id>[0-9]+)/$', job_views.JobDetails.as_view(), name='jobdetail'),
    url(r'^(?P<job_id>[0-9]+)/filled/$',login_required(job_views.JobMarkAsFilled.as_view()), name='job_filled'),
]
