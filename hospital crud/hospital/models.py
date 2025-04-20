from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)  # Shifoxona nomi
    address = models.CharField(max_length=500)  # Manzili
    established_year = models.PositiveIntegerField()  # Tashkil topgan yili

    def __str__(self):
        return self.name


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')
    full_name = models.CharField(max_length=255)  # Doktorning to‘liq ismi
    specialty = models.CharField(max_length=100)  # Mutaxassisligi
    experience_years = models.PositiveIntegerField()  # Ish tajribasi (yillar)

    def __str__(self):
        return f"{self.full_name} ({self.specialty})"