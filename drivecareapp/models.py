from django.db import models
from django.shortcuts import render
from django.template.defaulttags import comment

ROLE=[
    ('user','user'),
    ('Garages','Garages'),
]
STATUS=[
    ('active','active'),
    ('inactive','inactive'),
]
MODE=[('online','online'),
    ('offline','offline'),
]
PAYMENT_STATUS=[
    ('completed','completed'),
    ('uncompleted','uncompleted'),
]
# Create your models here.
# create class for registertable
class logintable(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    password = models.CharField(max_length=30)
    role=models.CharField(max_length=30,choices=ROLE)
    phone=models.BigIntegerField()
    status=models.CharField(max_length=30,choices=STATUS)
    timestamp=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class contactpage(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    phone= models.BigIntegerField()
    massage= models.TextField()
    timestamp=models.DateTimeField(auto_now=True)


class category(models.Model):
    cat_name= models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name


SERVICE_STATUS=[
    ('Available','Available'),
    ('Unavailable', 'Unavailable'),
]

class services(models.Model):
    cat_id=models.ForeignKey(category,on_delete=models.CASCADE)
    garage_id=models.ForeignKey(logintable,on_delete=models.CASCADE)
    service_name=  models.CharField(max_length=30)
    service_price=models.FloatField()
    service_desc = models.TextField()
    status= models.CharField(max_length=30,choices=SERVICE_STATUS)
    timestamp= models.DateTimeField(auto_now=True)

# user_profile
class userprofile(models.Model):
  username=models.ForeignKey(logintable,on_delete=models.CASCADE)
  address=models.CharField(max_length=50)
  date_of_birth=models.DateField()
  profession=models.CharField(max_length=20)
  bio = models.CharField(max_length=100)
  userprofile_image=models.ImageField(upload_to='')
# Location
class location(models.Model):
  Location_name = models.CharField(max_length=50)
#


# garages profile
class garage_profile(models.Model):
    username =models.ForeignKey(logintable,on_delete=models.CASCADE)
    location_name= models.ForeignKey(location,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    garage_profile_image=models.ImageField(upload_to='')
    garage_name= models.CharField(max_length=100)
    garage_address=models.CharField(max_length=255)
    year_of_experience=models.IntegerField()
    specialization=models.CharField(max_length=255)
    rating=models.FloatField()
    availability=models.CharField(max_length=40,choices=STATUS)


# service
class services_garages(models.Model):
    garage=models.ForeignKey(garage_profile,on_delete=models.CASCADE)
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()
    service_images=models.ImageField(upload_to='')
    service_availability=models.CharField(max_length=40,choices=STATUS)
# booking request

class booking_request(models.Model):
    user=models.ForeignKey(userprofile,on_delete=models.CASCADE)
    show_garage=models.ForeignKey(garage_profile,on_delete=models.CASCADE)
    # services=models.ManyToManyField(services)
    total_price=models.DecimalField(max_digits=20,decimal_places=2)
    vehicle_type=models.CharField(max_length=40)
    vehicle_name=models.CharField(max_length=40)
    booking_date=models.DateField()
    status=models.CharField(max_length=40,choices=STATUS)

# payment
class payment_details(models.Model):
    user=models.ForeignKey(userprofile,on_delete=models.CASCADE)
    booking_request=models.ForeignKey(booking_request,on_delete=models.CASCADE)
    amount=models.IntegerField()
    payment_date=models.DateTimeField()
    payment_mode=models.CharField(max_length=25,choices=MODE)
    razorpay_order_id=models.CharField(max_length=255)
    razorpay_payment_id=models.CharField(max_length=255)
    razorpay_signature=models.CharField(max_length=255)
    offline_reference=models.CharField(max_length=255)
    offline_remarks=models.TextField()
    address=models.TextField()
    status=models.CharField(max_length=40,choices=PAYMENT_STATUS)

    # payment_status=models.CharField(max_length=25,choices=STATUS)
# FEEDback
class Feedback(models.Model):
  user=models.ForeignKey(userprofile,on_delete=models.CASCADE)
  rating=models.IntegerField()
  comment=models.CharField(max_length=300)
  timestamp=models.DateTimeField(auto_now=True)

# complaints
class complaint(models.Model):
    user=models.ForeignKey(userprofile,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    description=models.TextField()
    timestamp=models.DateTimeField(auto_now=True)
