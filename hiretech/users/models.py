from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group

from  accounts.models import Account

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    account = models.ForeignKey('accounts.Account',blank=True,null=True)
    avatar = models.ImageField(upload_to=settings.MEDIA_ROOT,default='',blank=True)


def __unicode__(self):
        return '%s (%s)' % (
            self.user.username,
            self.user.account
        )
def user(self):
    return self.user.username
