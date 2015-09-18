import os
from django.conf import settings
from django.core.files import File

from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpRequest
from django.test import TestCase
from accounts.models import Account
from companies.models import Company
from jobs.models import Job
from .models import UserProfile
from .views import SignupView,DashboardView

# Create your tests here.
class LogoutViewTest(TestCase):
    def test_logout_response(self):
        url = '/logout/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

class LoginViewTest(TestCase):
    def setUp(self):
        image_source = '/tests/testdata/test-logo.png'
        self.image_path = os.path.join(settings.SITE_ROOT + image_source)

    def test_login_response(self):
        url = '/login/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_user_login(self):
        account = Account.objects.create(
            name='Alex Company',
            account_type='employer'
        )
        user = User.objects.create_user(
            username='alex@admin.com',
            email='alex@admin.com',
            first_name='Alex',
            last_name='Phelps',
            password='testpass'
            )
        company = Company.objects.create(
            account=account,
            company_name='Alex Company',
            company_logo= File(open(self.image_path)),
        )
        userprofile = UserProfile.objects.create(
            user=user,
            account=account,
        )
        url = '/login/'
        userdata = {
            'email':'alex@admin.com',
            'password':'testpass'
        }
        response = self.client.post(url,data=userdata,follow=True)
        self.assertRedirects(response,'/dashboard/',302)
        self.assertEqual(response.status_code,200)


class PasswordResetViewTest(TestCase):
    def setUp(self):
        image_source = '/tests/testdata/test-logo.png'
        self.image_path = os.path.join(settings.SITE_ROOT + image_source)

    def test_password_reset_response(self):
        url = '/password/reset/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_password_reset_form(self):
        account = Account.objects.create(
            name='Alex Company',
            account_type='employer'
        )
        user = User.objects.create_user(
            username='alex@admin.com',
            email='alex@admin.com',
            first_name='Alex',
            last_name='Phelps',
            password='testpass'
            )
        company = Company.objects.create(
            account=account,
            company_name='Alex Company',
            company_logo= File(open(self.image_path)),
        )
        userprofile = UserProfile.objects.create(
            user=user,
            account=account,
        )
        url = '/password/reset/'
        userdata = {
            'email':'alex@admin.com'
        }
        response = self.client.post(url,data=userdata,HTTP_HOST='example.com')
        self.assertEqual(response.status_code,200)



class SignupViewTest(TestCase):
    def setUp(self):
        image_source = '/tests/testdata/test-logo.png'
        self.image_path = os.path.join(settings.SITE_ROOT + image_source)

    def test_signup_response(self):
        url = '/join/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_signup_new_company(self):
        url = '/join/'
        test_logo = File(open(self.image_path))
        user_company_data = {
            'first_name':'Alex',
            'last_name':'Phelps',
            'email':'alex@admin.com',
            'password':'testpass',
            'company_name':'Alex Company',
            'company_logo':test_logo,
            'g-recaptcha-response': 'PASSED',
        }
        response = self.client.post(url,data=user_company_data,follow=True)
        self.assertRedirects(response,'/dashboard/',302)
        self.assertEqual(response.status_code,200)

class DashboardViewPublishedJobTest(TestCase):
    def setUp(self):
        image_source = '/tests/testdata/test-logo.png'
        self.image_path = os.path.join(settings.SITE_ROOT + image_source)

    def test_login_response(self):
        url = '/login/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_user_login(self):
        account = Account.objects.create(
            name='Alex Company',
            account_type='employer'
        )
        user = User.objects.create_user(
            username='alex@admin.com',
            email='alex@admin.com',
            first_name='Alex',
            last_name='Phelps',
            password='testpass'
            )
        company = Company.objects.create(
            account=account,
            company_name='Alex Company',
            company_logo= File(open(self.image_path)),
        )
        userprofile = UserProfile.objects.create(
            user=user,
            account=account,
        )
        job = Job.objects.create(
            job_company=company,
            job_location='Owensboro, KY',
            job_title='Python Guy',
            job_description='',
            job_status='published',
            job_type='full_time'
        )
        url = '/login/'
        userdata = {
            'email':'alex@admin.com',
            'password':'testpass'
        }
        response = self.client.post(url,data=userdata,follow=True)
        self.assertRedirects(response,'/dashboard/',302)
        self.assertEqual(response.status_code,200)
        expected = '<li class="list-group-item"><div class="row">'
        expected += '<div class="col-md-7 col-sm-7 col-xs-6">'
        expected += '<img class="img-responsive img-rounded pull-left m-r-10 '
        expected += 'job-list-img" src="/media/' + str(company.company_logo_thumb) + '">'
        expected += '<h5><a href="/jobs/' + str(job.id) + '/">Python Guy</a><br>'
        expected += '<small>Owensboro, KY</small></h5></div>'
        expected += '<div class="col-md-3 col-sm-3 col-xs-4">'
        expected += '<ul class="list-unstyled text-center m-t-10">'
        expected += '<li><a href="/jobs/' + str(job.id) +'/"><span '
        expected += 'class="job-type full_time">Full Time</span></a></li><li>'
        self.assertContains(response,expected)
        expected = '</li></ul></div><div class="col-md-2 col-sm-2 col-xs-2 text-center">'
        expected += '<div class="btn-group m-t-10"><a class="btn btn-default btn-sm '
        expected += 'dropdown-toggle" data-toggle="dropdown" href="#">'
        expected += '<i class="fa fa-cog"></i></a><ul class="dropdown-menu"><li>'
        expected += '<a href="#" data-toggle="modal" data-target="#myModal"> '
        expected += 'Mark as Filled</a></li></ul></div></div></div></li>'
        self.assertContains(response,expected)

class UserSettingsViewTest(TestCase):
    def setUp(self):
        image_source = '/tests/testdata/test-logo.png'
        self.image_path = os.path.join(settings.SITE_ROOT + image_source)

    def test_user_settings(self):
        account = Account.objects.create(
            name='Alex Company',
            account_type='employer'
        )
        user = User.objects.create_user(
            username='alex@admin.com',
            email='alex@admin.com',
            first_name='Alex',
            last_name='Phelps',
            password='testpass'
            )
        company = Company.objects.create(
            account=account,
            company_name='Alex Company',
            company_logo= File(open(self.image_path)),
        )
        userprofile = UserProfile.objects.create(
            user=user,
            account=account,
        )
        url = '/login/'
        userdata = {
            'email':'alex@admin.com',
            'password':'testpass'
        }
        response = self.client.post(url,data=userdata,follow=True)
        self.assertRedirects(response,'/dashboard/',302)
        self.assertEqual(response.status_code,200)
        url = '/users/settings/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
