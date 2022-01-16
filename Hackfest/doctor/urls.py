
from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctorHome),
    path('/patient-list/', views.patientList),
    path('/patient-list/patient/<int:id>', views.patientRecord),
    path('/patient-list/patient/addprescription/', views.addMedicineOnPrescription)
]
