from PIL import Image

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit,ResizeToFill
from taggit.managers import TaggableManager

from accounts.models import Account

class LogoProcessor(ImageSpec):
    format = 'JPEG'
    options = {'quality': 90}
    @property
    def processors(self):
        logoimage = self.source
        image = Image.open(logoimage)
        rgb_image = image.convert('RGB')
        background_color = rgb_image.getpixel((1, 1))
        if background_color == (0, 0, 0):
            background_color = (255,255,255)
        return [ResizeToFit(300, 300,mat_color=(background_color))]

register.generator('logo_processor', LogoProcessor)

class Company(models.Model):
    account = models.ForeignKey('accounts.Account',blank=True,null=True)
    company_name = models.CharField(max_length=200,default='')
    company_slug = models.SlugField(max_length=255, blank=True)
    company_url = models.URLField(max_length=200,default='')
    company_logo = models.ImageField(upload_to=settings.MEDIA_ROOT,default='')
    company_logo_thumb = ImageSpecField(
            source='company_logo',
            id='logo_processor'
        )
    company_featured_image = models.ImageField(upload_to=settings.MEDIA_ROOT,default='',blank=True)
    company_featured_image_thumb = ImageSpecField(
            source='company_featured_image',
            processors=[ResizeToFill(1200, 500)],
            format='JPEG',
            options={'quality': 95}
        )
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.company_name

    def save(self,**kwargs):
        if self.company_name and not self.company_slug:
            self.company_slug = slugify(self.company_name)
        return super(Company, self).save(**kwargs)

    def get_absolute_url(self):
        return "/companies/%s/" % self.company_slug
