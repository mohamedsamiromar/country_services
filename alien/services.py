from django.contrib.auth.models import Group
from .models import Alien


class AlineServices:
    @staticmethod
    def register_alien(
            first_name: str,
            last_name: str,
            email: str,
            gender: str,
            password: str,
            username: str,
            mobile_number: str,
            longitude: str,
            latitude: str,
            country: str
    ) -> Alien:
        new_alien = Alien(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender= gender,
            username=username,
            password=password,
            mobile_number=mobile_number,
            longitude=longitude,
            latitude=latitude,
            country=country,
        )

        return new_alien
