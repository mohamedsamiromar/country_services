from django.db import models
from django.conf import settings


class CurrentLocation(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=False, blank=True)
    country = models.CharField(
        max_length=55, null=True, blank=True, default=False)
    city = models.CharField(
        max_length=75, null=True, default=False)
    region_name = models.CharField(
        max_length=75, null=True, default=False)
    longitude = models.CharField(max_length=20, null=True, blank=True, default=False)
    latitude = models.CharField(max_length=20, null=True, blank=True, default=False)

    def __str__(self):
        return self.country
