from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.location_name

class Job(models.Model):
    job_category = models.ForeignKey(Category,default=0)
    job_location = models.ForeignKey(Location,default=0)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    pub_date = models.DateTimeField('date published')
