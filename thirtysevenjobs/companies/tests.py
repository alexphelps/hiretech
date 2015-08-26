from django.test import TestCase
from .models import Company
from jobs.models import Job, Category

# Create your tests here.
class CompanyDetailsViewTest(TestCase):
    def test_company_details_response(self):
        company = Company.objects.create(
            company_name='Pronto',
            company_logo='/media/logo.png',
            company_url='http://python.com',
        )
        url = '/companies/' + str(company.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_company_details_shows(self):
        category = Category.objects.create(category_name='Python Developer')
        company = Company.objects.create(
            company_name='Python Shop',
            company_logo='/media/logo.png',
            company_url='http://python.com',
        )
        job = Job.objects.create(
            job_category=category,
            job_company=company,
            job_location='Owensboro, KY',
            job_title='Python Guy',
            job_description='',
        )
        url = '/companies/' + str(company.id) + '/'
        response = self.client.get(url)
        expected = '<img class="img-responsive img-rounded" '
        expected += 'src="/media/logo.png" />'
        expected += '<h5 class="m-t-10">Python Shop</h5>'
        expected += '<p><a href="http://python.com" rel="nofollow">'
        expected += 'http://python.com</a></p>'
        self.assertContains(response,expected)
        expected = '<li class="list-group-item">'
        expected += '<div class="row"><div class="col-md-9 col-sm-9 col-xs-8">'
        expected += '<img class="img-responsive pull-left m-r-10 '
        expected += 'job-list-img" src="/media/logo.png">'
        expected += '<h5><a href="/jobs/1/">Python Guy</a><br>'
        expected += '<small>Owensboro, KY</small></h5></div>'
        expected += '<div class="col-md-3 col-sm-3 col-xs-4">'
        expected += '<ul class="list-unstyled text-center m-t-10"><li>'
        expected += '<a href="/jobs/1/"><span class="job-type full_time">'
        expected += 'Full Time</span></a></li><li><small class="timeago" '
        expected += 'title="">None</small></li></ul></div></div></li>'
        self.assertContains(response,expected)
