from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=200,null=False, blank=False)
    account_type_choices = (
        ('employer','Employer'),
        ('applicant','Applicant'),
    )
    account_type = models.CharField(max_length=20,choices=account_type_choices,default='employer')

    def __unicode__(self):
        return self.name
