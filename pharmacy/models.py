from django.db import models
from django.conf import settings
from location.models import CurrentLocation
from accounts.models import BaseModel


class Pharmacy(BaseModel):
    country = [
        ('FRA', 'French'),
        ('SWZ', 'Switzerland'),
        ('BLG', 'Belgium'),
    ]

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('P', 'Prefer not to answer'),
    )
    first_name = models.CharField(max_length=75, null=True, blank=True)
    last_name = models.CharField(max_length=75, null=True, blank=True)
    username = models.CharField(
        max_length=155, null=True, blank=True, default=False)
    password = models.CharField(max_length=75, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(
        max_length=255, null=True, blank=True, default=False)
    country = models.CharField(
        max_length=55, choices=country ,null=True, blank=True, default=False)
    city = models.CharField(
        max_length=75, null=True, default=False)
    start_time = models.CharField(max_length=75, null=True, blank=True)
    end_time = models.CharField(max_length=75, null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)


class DeliveryOrder(models.Model):
    alian = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, null=True,
                              blank=True)  # edit the relation when create model alian
    pharmacy = models.ForeignKey(Pharmacy,
                                 on_delete=models.CASCADE, null=True, blank=True, default=False)
    status = models.CharField(max_length=75,
                              choices=(
                                  (100, 'InOrder'),
                                  (201, 'WithDelivery'),
                                  (400, 'Delivered')), default=False
                              )
