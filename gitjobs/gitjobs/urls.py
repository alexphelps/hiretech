"""gitjobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from users import views as user_views
from search import views as search_views
from jobs.sitemap import JobsSiteMap
from companies.sitemap import CompaniesSiteMap

sitemaps = {
    'pages': FlatPageSitemap,
    'jobs-listings': JobsSiteMap,
    'companies': CompaniesSiteMap
}

urlpatterns = [
    url(r'^$', include('flatpages.urls', namespace="homepage")),
    url(r'^jobs/', include('jobs.urls', namespace="jobs")),
    url(r'^companies/', include('companies.urls', namespace="companies")),
    url(r'^users/', include('users.urls', namespace="jobs")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^join/$', user_views.SignupView.as_view(), name='signup'),
    url(r'^login/$', user_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', user_views.LogoutView.as_view(), name='logout'),
    url(r'^password/reset/$', user_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', user_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    url(r'^dashboard/$', login_required(user_views.DashboardView.as_view()), name='dashboard'),
    url(r'^search/', search_views.CustomSearchView.as_view(), name='search'),
    url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, {'sitemaps': sitemaps}),
]



admin.site.site_header = 'Gitjobs'
admin.site.site_name = 'Gitjobs'
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
