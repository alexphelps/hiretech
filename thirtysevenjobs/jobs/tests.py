from django.test import TestCase
from .models import Job
from companies.models import Company

# Create your tests here.
class JobIndexViewTest(TestCase):
    def test_index_response(self):
        url = '/jobs/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_job_list_shows(self):
        url = '/jobs/'
        company = Company.objects.create(
            company_name='Pronto',
            company_logo='/media/logo.png',
        )
        Job.objects.create(
            job_company=company,
            job_location='Owensboro, KY',
            job_title='Python Guy',
            job_description='',
        )
        response = self.client.get(url)
        expected = '<li class="list-group-item"><div class="row">'
        expected += '<div class="col-md-9 col-sm-9 col-xs-8">'
        expected += '<img class="img-responsive img-rounded pull-left m-r-10 job-list-img" '
        expected += 'src="/media/logo.png"><h5><a href="/jobs/3/">Python Guy</a>'
        expected += '<br><small><a href="/companies/4" class="text-muted">Pronto</a>'
        expected += ' - Owensboro, KY</small></h5></div><div class="col-md-3 col-sm-3 col-xs-4">'
        expected += '<ul class="list-unstyled text-center m-t-10"><li><a href="/jobs/3/">'
        expected += '<span class="job-type full_time">Full Time</span></a></li><li>'
        expected += '<small class="timeago" title="">None</small>'
        expected += '</li></ul></div></div></li>'
        self.assertContains(response,expected)

    def test_job_details_response(self):
        company = Company.objects.create(
            company_name='Python Shop',
            company_logo='/media/logo.png',
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
