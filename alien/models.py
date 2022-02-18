from django.db import models
from accounts.models import BaseModel
from core.validators import _NAME_REGEX
from location.models import CurrentLocation


class Alien(BaseModel):
    first_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[_NAME_REGEX], default=False)
    last_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[_NAME_REGEX], default=False)
    email = models.EmailField(
        unique=True, null=True)
    residence = models.ForeignKey(
        CurrentLocation, null=True, blank=True, default=False, related_name='current_location', on_delete=models.CASCADE)
    country = models.CharField(max_length=75, null=True, blank=True, default=False)
