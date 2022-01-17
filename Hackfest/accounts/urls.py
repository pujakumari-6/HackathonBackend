from django.urls import path
from . import views


urlpatterns = [
    path('/choise/createnurse/', views.addNurse),
    path('/choise/createdoctor/', views.addDoctor),
    path('/checkusercheck/<int:roleid>' ,views.doctor_register),
    path('/loginpage' , views.docter_login),
    path('/logout' , views.doctor_logout),
    path('/choise/', views.choiseview)
]