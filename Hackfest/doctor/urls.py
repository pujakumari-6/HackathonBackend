
from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctorHome),
    path('/patient-list/', views.patientList),
    path('/patient-list/patient/<int:patientId>', views.patientRecord,name='diagnosis'),
    path('/viewPrescription/<int:prescriptionId>', views.viewPrescription),
    path('/diagnosis/<int:patientId>', views.diagnosis),
    path('/medication/<int:prescriptionId>', views.medication),
    path('/searchpage/', views.searchPatient, name='searchlist'),
    path('/medicineFile/<int:prescriptionId>', views.medicineFile, name='medicineFile'),

]
