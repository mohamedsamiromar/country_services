from django.db import models
from accounts.models import BaseModel
from alien.models import Alien


class ParkingProfile(BaseModel):
    name = models.CharField(max_length=150, null=True, unique=True, blank=True)
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
    parking_number = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ParkingBooking(BaseModel):
    parking = models.ForeignKey(
        ParkingProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    alien = models.OneToOneField(
        Alien, on_delete=models.CASCADE, null=True, related_name='alien_parking', default=0)

    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)