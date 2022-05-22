from django.db import models

class CustomManager(models.Manager):
    def quadir(self, r1, r2):
        return super().get_queryset().filter(roll__range=(r1, r2)).order_by('id')