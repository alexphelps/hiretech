from django.test import TestCase
from .models import Company
from jobs.models import Job

# Create your tests here.
class CompanyDetailsViewTest(TestCase):
    def test_company_details_response(self):
        company = Company.objects.create(
            company_name='Git Jobs',
            company_logo='/media/logo.png',
            company_url='http://python.com',
        )
        url = '/companies/' + str(company.company_slug) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_company_details_shows(self):
        company = Company.objects.create(
            company_name='Git Jobs',
            company_logo='/media/logo.png',
            company_url='http://python.com',
        )
        job = Job.objects.create(
            job_company=company,
            job_location='Owensboro, KY',
            job_title='Python Guy',
            job_description='',
            job_status='published',
        )
        url = '/companies/' + str(company.company_slug) + '/'
        response = self.client.get(url)
        expected = '<img class="img-thumbnail job-details-img" src="/media/logo.png">'
        expected += '<h3>Git Jobs</h3><p>'
        expected += '<a href="http://python.com" rel="nofollow">http://python.com</a></p>'
        self.assertContains(response,expected)
        expected = '<li class="list-group-item">'
        expected += '<div class="row"><div class="col-md-9 col-sm-9 col-xs-8">'
        expected += '<img class="img-responsive pull-left m-r-10 job-list-img" '
        expected += 'src="/media/logo.png"><h5><a href="/jobs/1/">Python Guy</a>'
        expected += '<br><small>Owensboro, KY</small></h5></div>'
        expected += '<div class="col-md-3 col-sm-3 col-xs-4">'
        expected += '<ul class="list-unstyled text-center m-t-10">'
        expected += '<li><a href="/jobs/1/"><span class="job-type full_time">Full Time</span></a>'
        self.assertContains(response,expected)
