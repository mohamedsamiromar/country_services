from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import BaseModel


class Config(BaseModel):
    key = models.CharField(max_length=200, unique=True)
    value = models.TextField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_system = models.BooleanField(default=False)
    is_private = models.BooleanField(default=True)
    tag = models.CharField(max_length=100, blank=True, null=True)

    @property
    def _int(self):
        return int(self.value)

    @property
    def _float(self):
        return float(self.value)

    @property
    def _boolean(self):
        if self.value.lower() in ['true', 'yes', '1', 'yup']:
            return True
        else:
            return False
        # return bool(int(self.value))
