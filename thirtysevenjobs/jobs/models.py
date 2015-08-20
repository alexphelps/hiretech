from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.category_name

class Job(models.Model):
    job_category = models.ForeignKey(Category,default=0)
    job_company = models.ForeignKey('companies.Company',default=0)
    job_location = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    job_created_date = models.DateTimeField('date created',null=True)
    status_choices = (
        ('draft','Draft'),
        ('pending_review','Pending Review'),
        ('published','Published'),
        ('filled','Filled'),
    )
    job_status = models.CharField(max_length="20",choices=status_choices,default='draft')

    def __unicode__(self):
        return self.job_status
