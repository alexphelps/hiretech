from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200,default='')
    company_url = models.URLField(max_length=200,default='')
    def __unicode__(self):
        return self.company_name
