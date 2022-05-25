import re
from alien.models import Alien
from core.errors import APIError, Error
from hotel.models import  Hotel

def get_alien(id: int) -> Alien:
    try:
        alien = Alien.objects.get(pk=id)
    except Alien.DoesNotExist:
        raise APIError(Error.USER_NOT_FOUND)

def get_hotel(id: int) -> Hotel:
    try:
        Hotel.objects.get(pkp=id)
    except Hotel.DoesNotExist:
        raise APIError(Error.USER_NOT_FOUND)