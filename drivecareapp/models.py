from django.db import models
from django.shortcuts import render
ROLE=[
    ('user','user'),
    ('Garages','Garages'),
]
STATUS=[
    ('active','active'),
    ('inactive','inactive'),
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



class servicecategory(models.Model):
    cat_name= models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name

# SERVICE_STATUS=[
#     ('Available','Available'),
#     ('Unavailable', 'Unavailable'),
# ]
