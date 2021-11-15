from django.db import models
from django.contrib.auth.models import User


class CurrentLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    region_name = models.CharField(max_length=150, null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)

    def __str__(self):
        return self.country


class City(models.Model):
    city_1 = models.CharField(max_length=150, null=True)
    city_2 = models.CharField(max_length=150, null=True)
    city_3 = models.CharField(max_length=150, null=True)


class GetLocationManual(models.Model):
    country = models.CharField(max_length=150, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
