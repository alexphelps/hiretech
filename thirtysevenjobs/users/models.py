from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group

from  companies.models import Company

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name='user')
    company = models.ForeignKey('companies.Company', default='')

def __unicode__(self):
        return '%s (%s)' % (
            self.user.username,
            self.company.company_name
        )
def user(self):
    return self.user.username
