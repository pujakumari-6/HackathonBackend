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
    blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    age = models.PositiveIntegerField(default=0)
    Height = models.IntegerField

class PatientRecord(models.Model):
    PatientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Allergies = models.TextField(null=True,blank=False)
    Symptoms = models.TextField(null=True,blank=False)
    PregnancyStatus=models.BooleanField(default=False)
    PreviousSurgery = models.TextField(null=True,blank=False)
    IsDiabetic = models.BooleanField(default=False)
    InsurancePlanName = models.CharField( max_length=10, blank=True)
    Status = models.IntegerField(choices=STATUS)



