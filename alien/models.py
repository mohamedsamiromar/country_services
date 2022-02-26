from django.db import models
from accounts.models import BaseModel
from core.validators import _NAME_REGEX, _PHONE_REGEX


class Alien(BaseModel):
    user_types = [
        ('FRA', 'French'),
        ('SWZ', 'Switzerland'),
        ('BLG', 'Belgium'),
    ]

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('P', 'Prefer not to answer'),
    )
    first_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[_NAME_REGEX], default=False)
    last_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[_NAME_REGEX], default=False)
    email = models.EmailField(
        unique=True, null=True)
    gender = models.CharField(max_length=75, choices=GENDER_CHOICES, null=True, blank=True)
    username = models.CharField(max_length=10, unique=True, null=True)
    password = models.CharField(max_length=75, null=True, blank=True)
    mobile_number = models.CharField(
        max_length=15, validators=[_PHONE_REGEX], blank=True, null=True
    )
    longitude = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(
        max_length=75, null=True, blank=True, default=False, choices=user_types)

    REQUIRED_FIELDS = ['username', 'password', 'email']
