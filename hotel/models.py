from django.db import models
from accounts.models import BaseModel
from core.validators import _NAME_REGEX, _PHONE_REGEX
from alien.models import Alien
from accounts.models import CustomUser


class Hotel(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    name = models.CharField(max_length=150, null=True, blank=True, validators=[_NAME_REGEX])
    email = models.EmailField(unique=True, null=True, blank=True, default=False)
    longitude = models.CharField(max_length=20, null=True, blank=True, default=False)
    latitude = models.CharField(max_length=20, null=True, blank=True, default=False)

    phone_number = models.CharField(
        max_length=150, null=True, blank=True, default=False, validators=[_PHONE_REGEX])
    status = models.CharField(max_length=150, null=True, blank=True,
                              choices=(
                                  (100, 'New'),
                                  (201, 'Approve'),
                                  (400, 'Rejected')), default=100)


class Room(BaseModel):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name='hotel', null=True, blank=True)
    rooms_number = models.PositiveIntegerField(null=True, blank=True, default=False)
    floor = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=150, null=True, blank=True,
                              choices=(
                                  (100, 'not_completed'),
                                  (400, 'complete')), default=100)


class Booking(BaseModel):
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
