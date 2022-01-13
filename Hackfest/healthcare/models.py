from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
# Create your models here.

BLOOD_GROUP_CHOICE = (
    (1, _("A+")),
    (2, _("B+")),
    (3, _("O+")),
    (4, _("AB+")),
    (5, _("A-")),
    (6, _("B-")),
    (7, _("O-")),
    (8, _("AB-")),
)

STATUS = (
    (1, _("Recovered")),
    (2,_("Under Treatment"))
)

class Patient(models.Model):
    GENDER_CHOICE = (
        (1, _("Male")),
        (2,_("Female")),
        (3,_("Other")),
    )
    name = models.CharField(max_length=150, null=False,blank=False)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Please enter valid mobile number.")
    mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    email = models.EmailField(null=False,blank=False)
    registrationNumber = models.CharField(max_length=10)
    bloodGroup = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    age = models.PositiveIntegerField(default=0)
    height = models.IntegerField

class PatientRecord(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergies = models.TextField(null=True,blank=False)
    symptoms = models.TextField(null=True,blank=False)
    pregnancyStatus=models.BooleanField(default=False)
    previousSurgery = models.TextField(null=True,blank=False)
    isDiabetic = models.BooleanField(default=False)
    insurancePlanName = models.CharField( max_length=10, blank=True)
    status = models.IntegerField(choices=STATUS)



