from django.contrib import admin

# Register your models here.
from onetooneapp.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','designation','country']
admin.site.register(Profile,ProfileAdmin)