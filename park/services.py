from turtle import st
from folium import CssLink
from park.models import ParkPofile
from accounts.models import CustomUser


class ParkService:
    @staticmethod
    def create_park(
        username: str,
        email: str,
        first_name: str,
        last_name: str,
        name: str,
        mobile_number: int,
        country: str,
        city: str,
        address: str
    ) -> ParkPofile:
        park_user = CustomUser.objects.create(
            username = username,
            password = 123123,
            email= email,
            first_name = first_name,
            last_name= last_name
        )
        park = ParkPofile.objects.create(
            user= park_user, name=name, mobile_number=mobile_number, country=country, city=city, address=address)
        return park
        