from django.contrib import admin

# Register your models here.
from .models import Job
from .models import Category
from .models import Location

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title','job_category','job_location','pub_date')

admin.site.register(Job, JobAdmin)
admin.site.register(Category)
admin.site.register(Location)
