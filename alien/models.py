from django.db import models
from accounts.models import BaseModel
from core.validators import _NAME_REGEX, _PHONE_REGEX
from accounts.models import CustomUser


class Alien(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='alien_user', null=True, blank=True)
    first_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[_NAME_REGEX], default=False)
    last_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[_NAME_REGEX], default=False)
    email = models.EmailField(
        unique=True, null=True)
    password = models.CharField(max_length=75, null=True, blank=True)
    mobile_number = models.CharField(
        max_length=15, validators=[_PHONE_REGEX], blank=True, null=True
    )
    longitude = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=75, null=True, blank=True, default=False)
