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
    city_1 = models.CharField(max_length=150, null=True, default=False)
    city_2 = models.CharField(max_length=150, null=True, default=False)
    city_3 = models.CharField(max_length=150, null=True, default=False)

    def __str__(self):
        template = '{0.city_1} {0.city_2} {0.city_3}'
        return template.format(self)


class GetLocationManual(models.Model):
    country = models.CharField(max_length=150, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)


    def __str__(self):
        template = '{0.country} {0.city.city_1} {0.city.city_2} {0.city.city_3}'
        return template.format(self)


class SelecteCountryAndCity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
