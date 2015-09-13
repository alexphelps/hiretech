from django.contrib import admin

# Register your models here.
from .models import Account

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('name','account_type')
    list_filter = ['account_type']

admin.site.register(Account,AccountsAdmin)
