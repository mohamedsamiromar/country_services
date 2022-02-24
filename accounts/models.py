from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum


class GroupEnum(Enum):
    ADMIN_GROUP = 'Admin'
    ALIEN_GROUP = 'Alien'
    RESTURANT_GROUP = 'Resturant'


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

    class Meta:
        ordering = ('username', 'email', 'password')

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save()(*args, **kwargs)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    country_code = models.CharField(max_length=200)
    name = models.CharField(choices=(
        ('FRA', 'France'),
        ('SWZ', 'Switzerland'),
        ('BLG', 'Belgium'),
    ), blank=True, null=True, max_length=150, default=False
    )

    def __str__(self):
        return self.name


class LoginLog(BaseModel):
    username = models.CharField(max_length=11)

    def __str__(self):
        return '{} Logged in at {}'.format(self.username, self.created_at)
