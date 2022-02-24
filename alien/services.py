from location.models import CurrentLocation
from .models import Alien
from accounts.models import CustomUser


class AlineServices:
    @staticmethod
    def register_alien(
            user: CustomUser,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            mobile_number: str,
            longitude: str,
            latitude: str,
            country: str
    ) -> Alien:
        alia_regit = Alien(
            user=user,
            first_name=first_name,
            last_name=last_name,
            country=country,
            email=email,
            password=password,
            mobile_number=mobile_number,
            longitude=longitude,
            latitude=latitude
        )
        alia_regit.save()
        return alia_regit
