from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=200,null=False, blank=False)
    created_date = models.DateTimeField('date created',auto_now_add=True,null=True)
    owner = models.ForeignKey('auth.User',blank=True,null=True)
    account_type_choices = (
        ('employer','Employer'),
        ('applicant','Applicant'),
    )
    account_type = models.CharField(max_length=20,choices=account_type_choices,default='employer')
    free = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
