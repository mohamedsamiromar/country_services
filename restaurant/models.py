from location import models
from location.models import *
from django.conf import settings
from accounts.models import BaseModel
from core.validators import _NAME_REGEX, _PHONE_REGEX


class ResturantProfile(BaseModel):
    name = models.CharField(
        max_length=150, null=True, blank=True, default=False, validators=[_NAME_REGEX])
    mobile_number = models.CharField(
        max_length=15, null=True, blank=True, validators=[_PHONE_REGEX])
    address = models.CharField(max_length=155, null=True, blank=True, default=False)
    email = models.EmailField(unique=True, null=True, blank=True, default=False)
    menu = models.ForeignKey('Menu',
                             on_delete=models.CASCADE,
                             null=True, blank=True, default=False)
    country = models.CharField(
        max_length=55, null=True, blank=True, default=False)
    city = models.CharField(
        max_length=75, null=True, default=False)

    longitude = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)

    start_working = models.CharField(max_length=35, null=True, blank=True, default=False)
    end_working = models.CharField(max_length=35, null=True, blank=True, default=False)

    occupied_table = models.CharField(max_length=35, null=True, blank=True)
    available_table = models.CharField(max_length=35, null=True, blank=True)
    status = models.CharField(max_length=155, choices=(
        (201, 'Open'),
        (405, 'Closed'),
    ), default='Open')

    resturant_status = models.IntegerField(
        choices=(
            (200, 'New'),
            (201, 'Approved'),
            (400, 'Rejected'),
        ), default=200
    )
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Menu(BaseModel):
    sandwiches = models.CharField(max_length=155, choices=(
        ('meat', 'meat'),
        ("chicks", "chicks"),
        ("cheese", "cheese")
    ), default=False, null=True, blank=True)
    meal = models.CharField(max_length=155, choices=(
        ('meat', 'meat'),
        ("chicks", "chicks"),
        ("cheese", "cheese")
    ), default=False, null=True, blank=True)


class DelivaryOrder(BaseModel):
    alian = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, null=True, blank=True)
    resturant = models.ForeignKey(ResturantProfile,
                                  on_delete=models.CASCADE, null=True, blank=True)
    order_count = models.IntegerField(null=True, blank=True)
    user_mobile_number = models.CharField(max_length=11, null=True, blank=True)


class ResturantBookingTable(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_mobile_number = models.CharField(max_length=11, null=True, blank=True)
    table_booking_number = models.IntegerField(null=True, blank=True)
    chair_booking_number = models.IntegerField(null=True, blank=True)
    booking_hourse = models.CharField(max_length=150, null=True, blank=True)
