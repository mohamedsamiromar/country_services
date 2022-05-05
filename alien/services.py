from django.contrib.auth.models import Group
from .models import Alien


class AlineServices:
    @staticmethod
    def register_alien(
            gender: str,
            mobile_number: str,
            longitude: str,
            latitude: str,
            country: str
    ) -> Alien:
        new_alien = Alien(
            gender= gender,
            mobile_number=mobile_number,
            longitude=longitude,
            latitude=latitude,
            country=country,
        )
        new_alien.save()

        return new_alien
