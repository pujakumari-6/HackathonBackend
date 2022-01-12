from django.db import models

from healthcare.models import Patient

# Create your models here.
class Prescription(models.Model):
    PatientRecordId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Diagnosis = models.CharField(max_length=1000,null=False,blank=False)
    Medication = models.CharField(max_length=1000, null=True, blank=False)
    Dose = models.CharField(max_length=1000, null=True, blank=False)
    Duration = models.IntegerField(null=True, blank=False)

