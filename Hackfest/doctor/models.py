from django.db import models

from healthcare.models import Patient

# Create your models here.
class Prescription(models.Model):
    patientRecordId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=1000,null=False,blank=False)
    medication = models.CharField(max_length=1000, null=True, blank=False)
    dose = models.CharField(max_length=1000, null=True, blank=False)
    duration = models.IntegerField(null=True, blank=False)

