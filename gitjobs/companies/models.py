from PIL import Image

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from taggit.managers import TaggableManager

from accounts.models import Account

class LogoThumbnailProcessor(ImageSpec):
    format = 'JPEG'
    options = {'quality': 90}
    @property
    def processors(self):
        logoimage = self.source
        image = Image.open(logoimage)
        rgb_image = image.convert('RGB')
        r,g,b = rgb_image.getpixel((1, 1))
        return [ResizeToFit(300, 300,mat_color=(r,g,b))]

register.generator('companies:company:company_logo_thumbnail', LogoThumbnailProcessor)

class Company(models.Model):
    account = models.ForeignKey('accounts.Account',blank=True,null=True)
    company_name = models.CharField(max_length=200,default='')
    company_slug = models.SlugField(max_length=255, blank=True)
    company_url = models.URLField(max_length=200,default='')
    company_logo = models.ImageField(upload_to=settings.MEDIA_ROOT,default='')
    company_logo_thumb = ImageSpecField(
            source='company_logo',
            id='companies:company:company_logo_thumbnail'
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
