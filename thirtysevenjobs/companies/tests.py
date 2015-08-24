from django.test import TestCase
from .models import Company
from jobs.models import Job

# Create your tests here.
class CompanyDetailsViewTest(TestCase):
    def test_job_details_response(self):
        company = Company.objects.create(
            company_name='Pronto',
            company_logo='/media/logo.png',
        )
        url = '/companies/' + str(company.id) + '/'
        response = self.client.get(url)
        
