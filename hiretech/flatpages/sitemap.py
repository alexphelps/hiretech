from django.conf.urls import url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap


class FlatPageSitemap(FlatPageSitemap):
    changefreq = "daily"
    priority = 1
