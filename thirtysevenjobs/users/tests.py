from django.test import TestCase

# Create your tests here.
class SignupViewTest(TestCase):
    def test_signup_response(self):
        url = '/join/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
