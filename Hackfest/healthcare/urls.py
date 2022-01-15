from django.contrib import admin
from django.urls import path
from healthcare import views

urlpatterns = [
    path('/newPatient', views.newPatient, name='newPatient'),
    path('/patientRecord/<patientId>', views.patientRecord, name='patientRecord'),
    path('/updatePatientRecord/<patientId>', views.updatePatientRecord, name='updatePatientRecord'),
]
