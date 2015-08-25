from django.contrib import admin

from .models import UserProfile
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user','company')

admin.site.register(UserProfile, UsersAdmin)
