from django.contrib import admin

# Register your models here.
from .models import Job
from .models import Category
from .models import Location

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title','job_company','job_category','job_location','job_created_date','job_status')
    list_filter = ['job_status']
    search_fields = ['job_title']

admin.site.register(Job, JobAdmin)
admin.site.register(Category)
admin.site.register(Location)
