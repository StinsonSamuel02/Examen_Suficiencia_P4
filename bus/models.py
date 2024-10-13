from django.db import models
from route.models import Route


# Create your models here.
class Bus(models.Model):
    plate = models.CharField(max_length=15, unique=True)
    number = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField(default=4)

    route = models.ForeignKey(Route, related_name='route', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Bus: {self.number}'
