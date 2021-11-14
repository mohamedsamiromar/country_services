from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class CurrentLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    region_name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.city
