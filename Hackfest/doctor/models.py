from django.contrib.auth.models import User
from django.db import models


from healthcare.models import Patient
from django.contrib.auth.models import User
# Create your models here.

class Prescription(models.Model):
    prescriptionId = models.AutoField(primary_key=True)
    prescriptionPatient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=False, blank=False)
   

    def __int__(self):
        return self.prescriptionId

class Medicine(models.Model):
    medicineId = models.AutoField(primary_key=True)
    medicineName = models.CharField(max_length=25, blank=False, null=False)
    singleUnitQuantity = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.medicineName


class PrescribedMedicine(models.Model):
    prescribedMedicineId = models.AutoField(primary_key=True)
    prescribedMedicineDuration = models.CharField(
        max_length=11, null=False, blank=False)
    prescribedMedicineMedicine = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, null=False, blank=False)
    prescribedMedicineQuantity = models.CharField(max_length=11)
    prescribedMedicineTakenQuantity = models.CharField(max_length=11)
    prescribedMedicineInstructions = models.TextField(max_length=50)
    prescribedMedicineDiagnosis = models.TextField(max_length=50)
    prescribedMedicinePrescription = models.ForeignKey(
        Prescription, on_delete=models.CASCADE, null=False, blank=False)

    def __int__(self):
        return self.prescribedMedicineId

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    forgot_password_token= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
