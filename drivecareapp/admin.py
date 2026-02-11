from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

class Userdata(admin.ModelAdmin):
    list_display=['name','email','phone','password','role','status','timestamp']

admin.site.register(logintable, Userdata)

class contactdata(admin.ModelAdmin):
    list_display_contact = ['name', 'email', 'phone', 'message','timestamp']
admin.site.register(contactpage,contactdata)


class showcat(admin.ModelAdmin):
    list_display = ['id','cat_name']
admin.site.register(category,showcat)

class showservices(admin.ModelAdmin):
    list_display = ['id','cat_id','garage_id','service_name','service_price','service_desc','status','timestamp']
admin.site.register(services,showservices)

class user_profile(admin.ModelAdmin):
        list_display = ['username','address','date_of_birth','profession','bio','userprofile_image']
admin.site.register(userprofile,user_profile)

class location_detect(admin.ModelAdmin):
    list_display = ['Location_name']

admin.site.register(location,location_detect)

class garage_profile_details(admin.ModelAdmin):
    list_display = ['username','location_name','address','garage_profile_image','garage_name','garage_address','year_of_experience','specialization','rating','availability']

admin.site.register(garage_profile, garage_profile_details)

class services_garages_details(admin.ModelAdmin):
    list_display = ['garage','category','name','price','description','service_images','service_availability']

admin.site.register(services_garages,services_garages_details)

class booking_request_details(admin.ModelAdmin):
    list_display = ['user','show_garage','total_price','vehicle_type','vehicle_name','booking_date','status']
  # def show_services(self,obj):
  # #     return ",".join([str(f) for f in obj.services.all()])
  # # show_services.short_description = 'Services'

admin.site.register(booking_request,booking_request_details)

class payment_data_details(admin.ModelAdmin):
    list_display = ['user','booking_request','amount','payment_date','payment_mode','razorpay_order_id','razorpay_payment_id','razorpay_signature','offline_reference','offline_remarks','address','status']

admin.site.register(payment_details,payment_data_details)

class Feedback_details(admin.ModelAdmin):
    list_display = ['user','rating','comment','timestamp']
admin.site.register(Feedback,Feedback_details)

class complaints_details(admin.ModelAdmin):
    list_display = ['user','subject','description','timestamp']
admin.site.register(complaint,complaints_details)