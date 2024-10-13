from django.db import models
from bus.models import Bus


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cid = models.CharField(max_length=11)
    driver_licence = models.CharField(max_length=8)

    bus = models.OneToOneField(Bus, related_name='employee', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
