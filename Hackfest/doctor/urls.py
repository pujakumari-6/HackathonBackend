
from django.urls import path
from . import views

urlpatterns = [
    path('/loginpg' , views.docter_login),
    path('/logout' , views.doctor_logout),
    path('/forgot', views.forgot_password),
    path('/uservalidate', views.ForgetPassword),
]
