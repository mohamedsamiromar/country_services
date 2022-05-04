from location import models
from location.models import *
from django.conf import settings
from accounts.models import BaseModel
from core.validators import _NAME_REGEX, _PHONE_REGEX
from alien.models import Alien
from rating.models import Rating
from accounts.models import CustomUser


class RestaurantProfile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, null=True, unique=True, blank=True)
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
    restaurant_status = models.CharField(max_length=155, choices=(
        (201, 'Open'),
        (405, 'Closed'),
    ), default=201, null=True, blank=True)

    status = models.IntegerField(
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


class DeliveryOrder(BaseModel):
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE, null=True, blank=True, related_name='order_alien')
    restaurant = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE, null=True, blank=True)


class RestaurantBooking(BaseModel):
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE, related_name='alien_restaurant', null=True, blank=True)
    restaurant = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE, related_name='restaurant_bookign',
                                   null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=(
        (101, 'New'),
        (210, 'Open'),
        (410, 'Closed')), default=101, null=True, blank=True, max_length=20)
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE)
