from django.db import models
from django.db.models.base import Model

class Student(models.Model):
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    mobile_no = models.IntegerField()
# Create your models here.
