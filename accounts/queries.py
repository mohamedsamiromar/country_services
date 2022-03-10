from alien.models import Alien
from accounts.models import CustomUser
from core.errors import APIError, Error


def get_alien_with(id: CustomUser) -> CustomUser:
    try:
        Alien.objects.get(pk=id)
    except Alien.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND)


def get_username(username: str):
    try:
        CustomUser.objects.filter(username=username).first()
    except CustomUser.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND)
