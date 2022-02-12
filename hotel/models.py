from contextlib import nullcontext
import email
from enum import Flag
from hashlib import blake2s
from logging import makeLogRecord
from operator import mod
from re import U
from statistics import mode
from tkinter import N
from unicodedata import name
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from django.forms import DateTimeField
from accounts.models import  BaseModel, CustomUser
from location.models import CurrentLocation
from core.validators import _NAME_REGEX, _PHONE_REGEX 
from alien.models import Alien
# Create your models here.


class Hotel(BaseModel):
    name = models.CharField(
        max_length=150, null=True, blank=True, validators=[_NAME_REGEX])
    email = models.EmailField(
        unique=True, null=True, blank=True, default=False)
    location = models.ForeignKey(
        CurrentLocation, on_delete=models.CASCADE, null=True, default=False)
    address_detal = models.CharField(
        max_length=250, null=True, blank=True, default=False)
    phone_number = models.CharField(
        max_length=150, null=True, blank=True, default=False, validators=[_PHONE_REGEX])
    status = models.CharField(
        max_length=150, null=True, blank=True,
        choices=(
            (100, 'New'),
            (201, 'Approve'),
            (400, 'Rejected')), default=False
        )


class Room(BaseModel):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, null=True, blank=True, default=False)
    rooms_number = models.PositiveIntegerField(
        null=True, blank=True, default=False)
    status = models.CharField(
        max_length=150, null=True, blank=True,
         choices=(
            (100, 'full'),
            (400, 'unfull')), default=False
    )


class Booking(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True, default=False
    )
    alien = models.ForeignKey(
        Alien, on_delete=models.CASCADE, null=True, blank=True
    )
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, null=True, blank=True, default=False
    )
    chech_in = models,DateTimeField()
    check_out = models.DateTimeField()