from django.contrib import admin

# Register your models here.
from .models import Company

class ComapnyAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_url','account')
    search_fields = ['company_name']

admin.site.register(Company, ComapnyAdmin)
