from django.db import models
from accounts.models import BaseModel, CustomUser
from core.validators import _NAME_REGEX, _PHONE_REGEX


class Alien(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, null=True, unique=True, blank=True)

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

    gender = models.CharField(max_length=75, choices=GENDER_CHOICES, null=True, blank=True)

    mobile_number = models.CharField(
        max_length=15, validators=[_PHONE_REGEX], blank=True, null=True
    )
    longitude = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    REQUIRED_FIELDS = ['username', 'password', 'email']
