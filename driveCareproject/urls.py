"""
URL configuration for driveCareproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from drivecareapp import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.registerpage),
    path('login',views.loginpage),
    path('fetchpage',views.fetchpage),
    path('homepage',views.index),
    path('about',views.about),
    # path('contact_us_data',views.contact_us_data),
    path('contact',views.contact),
    path('',views.dark_index_1),
    path('dark_homepage2',views.dark_index_2),
    path('404',views.error_404),
    path('index2',views.homepage2),
    path('index3',views.homepage_3),
    path('index4',views.homepage_4),
    path('index5',views.homepage_5),
    path('index6',views.homepage_6),
    path('cars',views.cars),
    path('dark_cars',views.cars),
    path('dark_cars_list',views.dark_car_list),
    path('cars_list',views.cars_list),
    path('car_single',views.car_single),
    path('car_dark_single',views.dark_car_single),
    path('quick_booking',views.quick_booking),
    path('booking',views.booking),
    path('checklogin',views.checklogin),
    path('logout',views.logout),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




