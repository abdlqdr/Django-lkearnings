from django.db import models

# Create your models here.

class user(models.Model):
    student_name = models.CharField(max_length=60, default='')
    teacher_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=59)
    password = models.CharField(max_length=34)
