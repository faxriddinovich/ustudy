from django.db import models

# Create your models here.
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)  # Mashina brendi (Toyota, BMW, va h.k.)
    model = models.CharField(max_length=100)  # Modeli (Camry, X5, va h.k.)
    year = models.IntegerField()  # Ishlab chiqarilgan yili
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narxi

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"