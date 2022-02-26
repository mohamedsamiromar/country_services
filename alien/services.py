from location.models import CurrentLocation
from .models import Alien
from accounts.models import CustomUser


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
        alia_regit = Alien(
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
        alia_regit.save()
        return alia_regit
