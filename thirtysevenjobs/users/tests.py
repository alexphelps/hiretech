from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .views import SignupView,DashboardView

# Create your tests here.
class SignupViewTest(TestCase):
    def test_signup_response(self):
        url = '/join/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

class DashboardviewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='alex@python.me',
            email='alex@python.me',
            password='top_secret'
        )
    def dashboardTest(self):
        request = self.factory.get('/dashboard/')
        request.user = self.user
        response = DashboardView(request)
        self.assertEqual(response.status_code,200)
