from xmlrpc.client import TRANSPORT_ERROR
from django.db import models


class CurrentLocation(models.Model):
    country = models.CharField(
        max_length=75, null=True, blank=True)
    city = models.CharField(
        max_length=75, null=True, blank=True
    )
    region_name = models.CharField(
        max_length=75, null=True, default=False)
    longitude = models.CharField(max_length=20, null=True, blank=True, default=False)
    latitude = models.CharField(max_length=20, null=True, blank=True, default=False)

    def __str__(self):
        return self.country
