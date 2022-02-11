from ast import alias
from itertools import count

from accounts.models import Country
from .models import Alien, Residence

class AlineServices:
    @staticmethod
    def register_alien(
        first_name: str,
        last_name: str,
        residence: Residence
    ) -> Alien:

        alia_regit= Alien(
            first_name = first_name,
            last_name = last_name,
            residence = residence
            country = Country
        )
        alia_regit.save
        return alia_regit