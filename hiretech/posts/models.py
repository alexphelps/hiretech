from django.conf import settings
from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    published_date = models.DateField(auto_now=True,null=True)
    category = models.ForeignKey('posts.Category')
    featured_image = models.ImageField(upload_to=settings.MEDIA_ROOT,default='')

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.title

    def save(self,**kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(**kwargs)
