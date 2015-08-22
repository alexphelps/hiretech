from django.conf.urls import patterns,url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<job_id>[0-9]+)/$', views.jobdetail, name='jobdetail'),
]
