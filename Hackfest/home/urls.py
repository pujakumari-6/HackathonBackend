from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.homePage, name=''),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('registrationNo', views.registrationNo, name='registrationNo'),
    path('registrationNoSubmit', views.registrationNoSubmit, name='registrationNoSubmit'),
]
