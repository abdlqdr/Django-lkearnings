from django.db import models
from django.db.models.base import Model

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()


class Teacher(models.Model):
    tname = models.CharField(max_length=70)
    empnum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()
