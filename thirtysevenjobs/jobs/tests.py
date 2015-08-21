from django.test import TestCase
from .models import Job,Category
from companies.models import Company

# Create your tests here.
class IndexViewTest(TestCase):
    def test_index_response(self):
        url = '/jobs/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_job_list_shows(self):
        url = '/jobs/'
        category = Category.objects.create(category_name='Python Developer')
        company = Company.objects.create(company_name='Pronto')
        Job.objects.create(
            job_category=category,
            job_company=company,
            job_location='Owensboro, KY',
            job_title='Python Guy',
            job_description='',
        )
        response = self.client.get(url)
        self.assertContains(response,'<li><a href="/jobs/1/">Python Guy</a> Owensboro, KY</li>')
