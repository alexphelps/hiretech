from PIL import Image

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import slugify

from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,blank=True)

    def __unicode__(self):
        return self.title

    def save(self,**kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(**kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,blank=True)
    body = models.TextField()
    published_date = models.DateField(auto_now=True,null=True)
    category = models.ForeignKey('posts.Category')
    author = models.ForeignKey('auth.User',blank=True,null=True)
    featured_image = models.ImageField(upload_to=settings.MEDIA_ROOT,default='')
    featured_image_thumbnail = ImageSpecField(
        source='featured_image',
        processors=[ResizeToFill(820, 320)],
        format='JPEG',
        options={'quality': 95}
    )

    def __unicode__(self):
        return self.title

    def save(self,**kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(**kwargs)

    def get_absolute_url(self):
        return "/blog/%s/" % self.slug
