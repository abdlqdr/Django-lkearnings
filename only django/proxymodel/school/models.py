from django.db import models
from .managers import CustomManager


# Create your models here.
class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    roll = models.IntegerField()

    objects = models.Manager()

class MyExamCenter(ExamCenter):
    abdul = CustomManager()
    
    class Meta:
        proxy = True
        ordering = ['cname']
        
    
        
    
