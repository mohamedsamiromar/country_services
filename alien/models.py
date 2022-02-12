import email
from statistics import mode
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from accounts.models import BaseModel
from core.validators import _NAME_REGEX
from location.models import CurrentLocation


class Residence(BaseModel):
    location = models.ForeignKey(
        CurrentLocation, null=True, blank=True, default=False, related_name='current_location', on_delete=models.CASCADE)


class Alien(BaseModel):
    first_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[_NAME_REGEX], default=False
    )

    last_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[_NAME_REGEX], default=False
    )
    email = models.EmailField(
        unique=True, null=True
        )
    residence = models.ForeignKey(
        'Residence', null=True, blank=True, default=True, on_delete=models.CASCADE
    )
    
    country = models.CharField(max_length=75, null=True, blank=True, default=False)
    