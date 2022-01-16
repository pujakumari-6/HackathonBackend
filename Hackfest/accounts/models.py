from django.db import models
from django.contrib.auth.models import User



class Role(models.Model):
    role= models.CharField(max_length=1000, default=None)

class UserroleMap(models.Model):
    user_id= models.IntegerField(max_length=1000, default=None)
    role_id= models.IntegerField(max_length=1000, default=None)