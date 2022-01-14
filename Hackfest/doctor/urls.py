
from django.urls import path
from . import views

urlpatterns = [
    path('/choise/createnurse/', views.addNurse),
    path('/choise/createdoctor/', views.addDoctor),
    path('/checkusercheck/<roleid>' ,views.doctor_register),
    path('/loginpage' , views.docter_login),
    path('/logout' , views.doctor_logout),
<<<<<<< HEAD
    path('/choise/', views.choiseview)
=======
    path('patient-list/', views.patientList)
>>>>>>> 5532b48fda7a1870d6b266aa7ac745f18b2ea023
]
