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
        userdata = logintable.objects.get(email=uemail,password=upassword)
        request.session['log_id'] =userdata.id
        request.session['log_name']=userdata.name
        request.session['log_email']=userdata.email
        request.session['log_role']=userdata.role
        request.session.save()
        messages.success(request,'Login Successful')
        return render(request,'index.html')
    except logintable.DoesNotExist:
        messages.error(request,'Login Unsuccessful')
    return render(request,'login.html')

def fetchpage(request):
   name=request.POST.get('name')
   email=request.POST.get('email')
   role=request.POST.get('role')
   phone=request.POST.get('phone')
   password=request.POST.get('password')
   status=request.POST.get('status')
   insert_query=logintable(name=name,email=email,role=role,phone=phone,password=password,status='active')
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

def error_404(request):
    return render(request,'404.html')
def cars(request):
    return render(request,'cars.html')

# quick-booking
def quickbooking(request):
    return render(request,'quickbooking.html')

def account_booking(request):
    return render(request,'accountbooking.html')

def account_dashboard(request):
    return render(request,'accountdashboard.html')

def account_profile(request):
    return render(request,'accountprofile.html')