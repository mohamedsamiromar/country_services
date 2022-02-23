from location.models import CurrentLocation
from .models import Alien


class AlineServices:
    @staticmethod
    def register_alien(
            first_name: str,
            last_name: str,
            country: str,
            email: str,
            username: str,
            password: str,
            mobile_number: str,
            longitude: str,
            latitude: str

    ) -> Alien:
        alia_regit = Alien(
            first_name=first_name,
            last_name=last_name,
            country=country,
            email=email,
            username=username,
            password=password,
            mobile_number=mobile_number,
            longitude=longitude,
            latitude=latitude
        )
        alia_regit.save()
        return alia_regit
