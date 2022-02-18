from django.db import models
from django.conf import settings
from location.models import CurrentLocation
from accounts.models import BaseModel


class Pharmacy(BaseModel):
    name = models.CharField(
        max_length=155, null=True, blank=True, default=False)
    address = models.CharField(
        max_length=255, null=True, blank=True, default=False)
    country = models.CharField(
        max_length=55, null=True, blank=True, default=False)
    city = models.CharField(
        max_length=75, null=True, default=False)
    region_name = models.CharField(
        max_length=75, null=True, default=False)
    location = models.ForeignKey(
        CurrentLocation, on_delete=models.CASCADE, null=True, blank=True, related_name='pharmacy_location')
    start_time = models.CharField(max_length=75, null=True, blank=True)
    end_time = models.CharField(max_length=75, null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(
        choices=(
            (200, 'New'),
            (201, 'Approved'),
            (400, 'Rejected'),
        ), default=200
    )


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
