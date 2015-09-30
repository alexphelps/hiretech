import os
from django.conf import settings
from django.core.files import File
from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
from .models import Post,Category

class BlogIndexViewTest(TestCase):
    def setUp(self):
        image_source = '/tests/testdata/test-logo.png'
        self.image_path = os.path.join(settings.SITE_ROOT + image_source)

    def test_posts_index_response(self):
        url = '/blog/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_post_single_response(self):
        user = User.objects.create_user(
            username='alex@admin.com',
            email='alex@admin.com',
            first_name='Alex',
            last_name='Phelps',
            password='testpass'
        )
        category = Category.objects.create(
            title='Test',
            slug='test'
        )
        post = Post.objects.create(
            title='Test Title',
            slug='test-slug',
            published_date='2015-08-21',
            category=category,
            author=user,
            status='published',
            featured_image=File(open(self.image_path)),
        )
        url = '/blog/' + post.slug + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
