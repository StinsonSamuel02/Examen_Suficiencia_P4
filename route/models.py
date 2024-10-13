from django.db import models


# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return f'Ruta: {self.name}|{self.origin}-{self.destination}'
