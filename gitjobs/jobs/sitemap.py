from django.conf.urls import url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap

from .models import Job

class JobsSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.job_created_date
