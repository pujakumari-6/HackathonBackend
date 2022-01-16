import datetime
from django.contrib.auth.models import User
from django.db import models


from healthcare.models import Patient
from django.contrib.auth.models import User
# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    form = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    concentration = models.CharField(max_length=100)
    unitOfPreparation = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    expiryDate = models.DateField()
    amount = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    description = models.TextField()
class Diagnosis(models.Model):
    diagnosisName = models.CharField(max_length=200)
    diagnosisBodySite = models.CharField(max_length=100)
    dateOfOnset = models.DateField()
    severity = models.CharField(max_length=50)
    dateOfAbatement = models.DateField()
    diagnosisCertainity= models.CharField(max_length=100)
    diagnosisDescription  = models.TextField()
    createdDate  = models.DateField(default=datetime.datetime.now)
class MedicalDevice(models.Model):
    deviceName = models.CharField(max_length=200)
    deviceBodySite = models.CharField(max_length=200)
    deviceUse = models.CharField(max_length=100)
    deviceDscription = models.CharField(max_length=100)
class LaboratoryTest(models.Model):
    testName = models.CharField(max_length=200)
    testSpecimen = models.CharField(max_length=100)
    testBodySite = models.CharField(max_length=200)
    testUse = models.CharField(max_length=100)
    testDescription = models.CharField(max_length=100)
class Prescription(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosisId = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    medicalDevice = models.ForeignKey(MedicalDevice, on_delete=models.CASCADE)
    laboratoryTestId = models.ForeignKey(LaboratoryTest, on_delete=models.CASCADE)

class MedicineDirection(models.Model):
    medicineId = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    doseUnit = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    doseTiming = models.CharField(max_length=100)
    additionalInstruction = models.TextField()
    reason = models.TextField()

class MedicineDirPrescriptionMap(models.Model):
    prescriptionId = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicineDirectionId = models.ForeignKey(MedicineDirection, on_delete=models.CASCADE)

   


   
