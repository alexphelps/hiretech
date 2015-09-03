from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200,default='')
    company_slug = models.SlugField(max_length=255, blank=True)
    company_url = models.URLField(max_length=200,default='')
    company_logo = models.ImageField(upload_to=settings.MEDIA_ROOT,default='')

    def __unicode__(self):
        return self.company_name

    def save(self,**kwargs):
        if self.company_name and not self.company_slug:
            self.company_slug = slugify(self.company_name)
        return super(Company, self).save(**kwargs) 
