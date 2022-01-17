import datetime
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=150, null=False)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Please enter valid mobile number.")
    mobile = models.CharField(validators=[phone_regex], max_length=10)
    email = models.EmailField(null=False,blank=False,unique=True)
    registrationNumber = models.CharField(max_length=50)
    bloodGroup = models.CharField(max_length=10, null=False)
    gender = models.CharField(max_length=20, null=False)
    dateOfBirth = models.DateField(null=False)
    createdDate = models.DateField(default=datetime.datetime.now)

class PatientRecord(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    bloodPressure = models.CharField(max_length=50)
    pulseRate = models.CharField(max_length=50)
    bodyTemprature = models.CharField(max_length=50)
    isAlcolohic = models.CharField(max_length=10)
    isSmoker = models.CharField(max_length=10)
    allergies = models.TextField(null=True)
    pregnancyStatus=models.CharField(max_length=5, null=True)
    estimatedDelivery=models.DateField(null=True)
    previousSurgery = models.TextField(null=True)
    isDiabetic = models.CharField(max_length=5, null=False)
    insurancePlanName = models.CharField( max_length=100,null=True)
    insurancePlanNumber = models.CharField( max_length=50, null=True)
    status = models.CharField(max_length=20, null=False)
    createdDate = models.DateField(default=datetime.datetime.now)
    updatedDate = models.DateField(default=datetime.datetime.now)

