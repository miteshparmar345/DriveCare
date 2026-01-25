from urllib import request
from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.
def registerpage(request):
    return render(request,'register.html')
def loginpage(request):
    return render(request,'login.html')

def checklogin(request):
    uemail = request.POST.get('email')
    upassword= request.POST.get('password')

    try:
        userdata = registertable.objects.get(email=uemail,password=upassword)
        request.session['log_id'] =userdata.id
        request.session['log_name']=userdata.name
        request.session['log_email']=userdata.email
        request.session['log_role']=userdata.role
        request.session.save()
        messages.success(request,'Login Successful')
        return render(request,'dark-index-1.html')
    except registertable.DoesNotExist:
        messages.error(request,'Login Unsuccessful')
    return render(request,'login.html')

def fetchpage(request):
   name=request.POST.get('name')
   email=request.POST.get('email')
   role=request.POST.get('role')
   phone=request.POST.get('phone')
   password=request.POST.get('password')
   status=request.POST.get('status')
   insert_query=registertable(name=name,email=email,role=role,phone=phone,password=password,status='active')
   insert_query.save()
   print("data inserted")
   return render(request,'login.html')

def logout(request):
    try:
        del request.session['log_id']
        del request.session['log_name']
        del request.session['log_email']
        del request.session['log_role']
        print("Logout Successful")
    except:
        print("Error Occured")
    return render(request,'login.html')


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
# def contact_us_data(request):
#     name=request.POST.get('name')
#     email=request.POST.get('email')
#     phone=request.POST.get('phone')
#     message=request.POST.get('message')
#     print(name)
#     # insert_query= contactpage(name=name,email=email,phone=phone,message=message)
#     # insert_query.save()
    return render(request,'contact.html')
def dark_index_1(request):
    return render(request,'dark-index-1.html')
def dark_index_2(request):
    return render(request,'02_dark-index-2.html')
def homepage2(request):
    return render(request,'index-2.html')
def homepage_3(request):
    return render(request,'index-3.html')
def homepage_4(request):
    return render(request,'index-4.html')
def homepage_5(request):
    return render(request,'index-5.html')
def homepage_6(request):
    return render(request,'index-6.html')
def error_404(request):
    return render(request,'404.html')
def cars(request):
    return render(request,'cars.html')
def dark_cars(request):
    return render(request,'02_dark-cars.html')
def dark_car_list(request):
    return render(request,'02_dark-cars-list.html')
def cars_list(request):
    return render(request,'cars-list.html')
def car_single(request):
    return render(request,'car-single.html')
def dark_car_single(request):
    return render(request,'02_dark-car-single.html')

# quick-booking
def quick_booking(request):
    return render(request,'quick-booking.html')
def booking(request):
    return render(request,'booking.html')