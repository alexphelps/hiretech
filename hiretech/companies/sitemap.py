from django.conf.urls import url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap

from .models import Company

class CompaniesSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Company.objects.all()
