from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from . import views as user_views

urlpatterns = [
    url(r'^settings/$', user_views.UserSettingsView.as_view(), name='user_settings'),
    url(r'^update-password/$', user_views.PasswordUpdateView.as_view(), name='user_settings'),
]
