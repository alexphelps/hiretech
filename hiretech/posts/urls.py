from django.conf.urls import patterns,url,include
from .models import Post,Category
from . import views as post_views

urlpatterns = [
    url(r'^$', post_views.PostIndex.as_view(), name='post_index'),
    url(r'^(?P<slug>[0-9A-Za-z\-]+)/$', post_views.PostSingle.as_view(), name='post_single'),
]
