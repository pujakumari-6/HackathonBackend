
from django.urls import path
from . import views

urlpatterns = [
    path('/loginpage', views.view_login ),
    path('/loginpg' , views.docter_login),
    path('/logout' , views.doctor_logout),



]
