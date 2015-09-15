from django.conf.urls import patterns,url
from . import views as flatpage_views

urlpatterns = [
    url(r'^$', flatpage_views.HomepageView.as_view(), name='homepage'),
]
