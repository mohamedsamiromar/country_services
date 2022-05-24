from hashlib import blake2s
from http import server
from re import S, T
import re
from statistics import mode
from tkinter.tix import Tree
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from accounts.models import BaseModel, CustomUser
from core.validators import _PHONE_REGEX
# Create your models here.


class ParkPofile(BaseModel):
    country = [
        ('FRA', 'French'),
        ('SWZ', 'Switzerland'),
        ('BLG', 'Belgium'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user_park', blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True, )
    country = models.CharField(max_length=55, choices=country, null=True, blank=True, default=False)
    city = models.CharField(max_length=55, null=True, blank=True)
    status = models.CharField(max_length=155, choices=(
            (201, 'Open'),
            (405, 'Closed'),
        ), default=201, null=True, blank=True)
    address = models.TextField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.name