from django.db import models
from accounts.models import BaseModel


class Parking(BaseModel):
    username = models.CharField(max_length=10, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(
        max_length=255, blank=True, null=True)
    last_name = models.CharField(
        max_length=255, blank=True, null=True)
    country = [
        ('FRA', 'French'),
        ('SWZ', 'Switzerland'),
        ('BLG', 'Belgium'),
    ]
    country = models.CharField(max_length=75, choices=country, null=True, blank=True)
    city = models.CharField(max_length=75, null=True, blank=True)
    region_name = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    status = models.IntegerField(
        choices=(
            (200, 'New'),
            (201, 'Approved'),
            (400, 'Rejected'),
        ), default=200
    )
