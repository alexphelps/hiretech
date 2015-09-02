from django.core.files import File
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from companies.models import Company
from .models import UserProfile
from .views import SignupView,DashboardView

# Create your tests here.
class LogoutViewTest(TestCase):
    def test_logout_response(self):
        url = '/logout/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

class LoginViewTest(TestCase):

    def test_login_response(self):
        url = '/login/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_user_login(self):
        user = User.objects.create_user(
            username='alex@admin.com',
            email='alex@admin.com',
            first_name='Alex',
            last_name='Phelps',
            password='testpass'
            )
        company = Company.objects.create(
            company_name='Alex Company',
            company_logo='/media/logo.png',
        )
        userprofile = UserProfile.objects.create(
            user=user,
            company=company,
            user_type='employer'
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
    def test_password_reset_response(self):
        url = '/password/reset/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

class SignupViewTest(TestCase):
    def test_signup_response(self):
        url = '/join/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_signup_new_company(self):
        url = '/join/'
        test_logo = open('static/admin/img/icon_alert.gif')
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
