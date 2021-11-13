from django.db import models

# Create your models here.
from datetime import time

from django.db import models
from django.contrib.auth.models import User


class ForgetPassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.IntegerField(null=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.user.username
