from django.contrib.auth.models import AbstractUser
from django.db import models
from location.models import *

# Create your models here.
from accounts.models import Country, BaseModel, CustomUser


class ResturantRegisterApplication(BaseModel):
    name = models.CharField(max_length=150, null=True, blank=True, )
    user_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="county_name")
    start_working = models.DateTimeField(null=True, blank=True)
    end_working = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=155, choices=(
        (201, 'Open'),
        ('CLS', 'Closed'),
    ), default='Open'
                              )


class ResturanProfile(BaseModel):
    name = models.CharField(max_length=150, null=True, blank=True, )
    address = models.CharField(max_length=155, null=True, blank=True)
    email = models.EmailField(unique=True)
    menu = models.ForeignKey('Menu',
                             on_delete=models.CASCADE,
                             related_name='resturan_menu',
                             null=True, blank=True)
    city = models.CharField(max_length=75, null=True, blank=True)
    country = models.CharField(max_length=75, null=True, blank=True)
    occupied_table = models.IntegerField(null=True, blank=True)
    available_table = models.IntegerField(null=True, blank=True)


class Menu(BaseModel):
    pass


class DelivaryOrder(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='username')
    resturant = models.ForeignKey(ResturanProfile, on_delete=models.CASCADE, name='resturant_name')
    order_count = models.IntegerField(null=True, blank=True)
    user_mobile_number = models.CharField(max_length=11, null=True, blank=True)


class ResturantBookingTable(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='username')
    user_mobile_number = models.CharField(max_length=11, null=True, blank=True)
    table_booking_number = models.IntegerField(null=True, blank=True)
    chair_booking_number = models.IntegerField(null=True, blank=True)
    booking_hourse = models.CharField(max_length=150, null=True, blank=True)
