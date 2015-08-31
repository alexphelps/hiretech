from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase

from .views import SignupView,DashboardView

# Create your tests here.
class LogoutViewTest(TestCase):
    def test_signup_response(self):
        url = '/logout/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

class LoginViewTest(TestCase):
    def test_signup_response(self):
        url = '/login/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

class PasswordResetViewTest(TestCase):
    def test_signup_response(self):
        url = '/password/reset/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

class SignupViewTest(TestCase):
    def test_signup_response(self):
        url = '/join/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
