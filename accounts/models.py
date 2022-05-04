from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum


class GroupEnum(Enum):
    ADMIN_GROUP = 'Admin'
    ALIEN_GROUP = 'Alien'
    Restaurant_GROUP = 'Restaurant'
    PHARMACY_GROUP = 'Pharmacy'
    PARKING_GROUP = 'Parking'
    HOTEL_GROUP = 'Hotel'


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=255, blank=True, null=True)
    last_name = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('username', 'email', 'password')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username', 'email', 'password')


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True


class LoginLog(BaseModel):
    username = models.CharField(max_length=11)

    def __str__(self):
        return '{} Logged in at {}'.format(self.username, self.created_at)
