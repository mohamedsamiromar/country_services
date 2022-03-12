from alien.models import Alien
from core.errors import APIError, Error
from accounts.models import CustomUser
from . models import ParkingProfile


def get_alien(id: int) -> Alien:
    try:
        Alien.objects.get(pk=id)
    except Alien.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND)


def get_parking(user: CustomUser) -> ParkingProfile:
    try:
        ParkingProfile.objects.get(pk=user)
    except ParkingProfile.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND)