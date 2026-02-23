from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

class Userdata(admin.ModelAdmin):
    list_display=['name','email','phone','password','role','status','timestamp']

# class contactdata(admin.ModelAdmin):
#     list_display_contact = ['name', 'email', 'phone', 'message']

admin.site.register(logintable,Userdata)
# admin.site.register(contactpage,contactdata)


class showcat(admin.ModelAdmin):
    list_display = ['id','cat_name']
admin.site.register(category,showcat)

class showservices(admin.ModelAdmin):
    list_display = ['id','cat_id','garage_id','service_name','service_price','service_desc','status','timestamp']
admin.site.register(services,showservices)
