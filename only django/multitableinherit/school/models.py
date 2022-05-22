from django.db import models

# Create your models here.

class ExamCenter(models.Model):
    ename = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class Student(ExamCenter):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    