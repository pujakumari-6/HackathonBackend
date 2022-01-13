from django.contrib.auth.models import User
from django.db import models


from healthcare.models import Patient
from django.contrib.auth.models import User
# Create your models here.
class Prescription(models.Model):
    PatientRecordId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Diagnosis = models.CharField(max_length=1000,null=False,blank=False)
    Medication = models.CharField(max_length=1000, null=True, blank=False)
    Dose = models.CharField(max_length=1000, null=True, blank=False)
    Duration = models.IntegerField(null=True, blank=False)

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    forgot_password_token= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
