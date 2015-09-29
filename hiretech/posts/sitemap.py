from django.conf.urls import url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap

from .models import Post

class PostsSiteMap(Sitemap):
    changefreq = "Weekly"
    priority = 0.7

    def items(self):
        return Post.objects.filter(status='published')
