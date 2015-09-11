from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from . import views as user_views

urlpatterns = [
    url(r'^(?P<user_profile_id>[0-9]+)/edit/$', user_views.UserEditView.as_view(), name='user'),
]
