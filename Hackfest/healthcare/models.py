import datetime
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=150, null=False,blank=False)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Please enter valid mobile number.")
    mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    email = models.EmailField(null=False,blank=False,unique=True)
    registrationNumber = models.CharField(max_length=50)
    bloodGroup = models.CharField(max_length=10, null=False,blank=False)
    gender = models.CharField(max_length=20, null=False,blank=False)
    dateOfBirth = models.DateField(null=False)
    createdDate = models.DateField(default=datetime.datetime.now)

class PatientRecord(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    height = models.IntegerField(null=True,blank=False)
    weight = models.IntegerField(null=True,blank=False)
    allergies = models.TextField(null=True,blank=False)
    pregnancyStatus=models.CharField(max_length=5, null=False,blank=False)
    previousSurgery = models.TextField(null=True,blank=False)
    isDiabetic = models.CharField(max_length=5, null=False,blank=False)
    insurancePlanName = models.CharField( max_length=100,null=True, blank=False)
    insurancePlanNumber = models.CharField( max_length=50, null=True, blank=False)
    status = models.CharField(max_length=20, null=False,blank=False)
    createdDate = models.DateField(default=datetime.datetime.now)
    updatedDate = models.DateField(default=datetime.datetime.now)

