from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

class Userdata(admin.ModelAdmin):
    list_display=['name','email','phone','password','role','status','timestamp']

class contactdata(admin.ModelAdmin):
    list_display_contact = ['name', 'email', 'phone', 'message']

admin.site.register(registertable,Userdata)
admin.site.register(contactpage,contactdata)



