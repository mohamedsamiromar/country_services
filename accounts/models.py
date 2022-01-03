from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=255, blank=True, null=True)
    middle_name = models.CharField(
        max_length=255, blank=True, null=True)
    last_name = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('username', 'email', 'password')

    def __str__(self):
        return self.username


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    country_code = models.CharField(max_length=2)
    dialing_code = models.CharField(max_length=4)
    name = models.CharField(choices=(
            ('FRa', 'France'),
            ('SWZ', 'Switzerland'),
            ('BLG', 'Belgium'),
        ), blank=True, null=True
    )

    def __str__(self):
        return self.name