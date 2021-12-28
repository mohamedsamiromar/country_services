from django.db import models
from location.models import *
# Create your models here.


class ResturantRegisterApplication(models.Model):
    name = models.CharField(
        max_length=155, null=True, blank=True, default=False)
    street = models.CharField(max_length=100, verbose_name="street")
    zip_code = models.CharField(max_length=100, verbose_name="zip code")
    resturant_type = models.CharField(
        max_length=255, null=True, blank=True, default=False)
    type = models.CharField(max_length=255, choices=(
        ("Br", 'Branch'),
        ("Ev", 'Event'),
        ("Other", 'Other'),
    ))

