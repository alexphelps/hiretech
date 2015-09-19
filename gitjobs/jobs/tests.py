import os
from django.conf import settings
from django.core.files import File

from django.test import TestCase
from .models import Job
from companies.models import Company

# Create your tests here.
class JobIndexViewTest(TestCase):
    def setUp(self):
        image_source = '/tests/testdata/test-logo.png'
        self.image_path = os.path.join(settings.SITE_ROOT + image_source)

    def test_index_response(self):
        url = '/jobs/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_job_list_shows(self):
        url = '/jobs/'
        company = Company.objects.create(
            company_name='Alex Test Company',
            company_logo= File(open(self.image_path)),
            company_slug='alex-test-company'
        )
        job = Job.objects.create(
            job_company=company,
            job_location='Owensboro, KY',
            job_title='Python Guy',
            job_description='',
            job_status='published',
        )
        response = self.client.get(url)
        expected = '<li class="list-group-item"><div class="row">'
        expected += '<div class="col-md-9 col-sm-9 col-xs-8">'
        expected += '<img class="img-responsive pull-left m-r-10 '
        expected += 'job-list-img" src="/media/'
        expected += str(company.company_logo_thumb) + '">'
        expected += '<h5><a href="/jobs/'+ str(job.id) +'/">Python Guy</a><br><small>'
        expected += '<a href="/companies/alex-test-company" class="text-muted">'
        expected += 'Alex Test Company</a> - Owensboro, KY</small></h5>'
        expected += '</div><div class="col-md-3 col-sm-3 col-xs-4">'
        expected += '<ul class="list-unstyled text-center m-t-10"><li>'
        expected += '<a href="/jobs/'+ str(job.id) +'/"><span class="job-type full_time">'
        expected += 'Full Time</span></a></li>'
        self.assertContains(response,expected)

    def test_job_details_response(self):
        company = Company.objects.create(
            company_name='Python Shop',
            company_logo= File(open(self.image_path)),
            company_url='http://python.com',
        )
        job = Job.objects.create(
            job_company=company,
            job_location='Owensboro, KY',
            job_title='Python Guy',
            job_description='',
        )
        url = '/jobs/' + str(job.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
