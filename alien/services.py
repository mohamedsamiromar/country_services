from location.models import CurrentLocation
from .models import Alien


class AlineServices:
    @staticmethod
    def register_alien(
            first_name: str,
            last_name: str,
            country: str,
            email: str,
            mobile_number: str,
            residence: CurrentLocation

    ) -> Alien:
        alia_regit = Alien(
            first_name=first_name,
            last_name=last_name,
            country=country,
            email=email,
            mobile_number=mobile_number,
            residence=residence
        )
        alia_regit.save()
        return alia_regit
