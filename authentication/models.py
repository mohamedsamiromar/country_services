from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import BaseModel


class ForgetPassword(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,null=True, blank=True, default=False)
    verification_code = models.IntegerField(null=True, blank=True, default=False)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.user, User.username
