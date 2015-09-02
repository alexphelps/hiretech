from django.conf.urls import patterns,url
from . import views as job_views

urlpatterns = [
    url(r'^$', job_views.JobIndex.as_view(), name='jobindex'),
    url(r'^add/$', job_views.JobAddNew.as_view(), name='jobadd'),
    url(r'^(?P<job_id>[0-9]+)/$', job_views.JobDetails.as_view(), name='jobdetail'),
]
