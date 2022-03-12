from django.contrib.auth.models import Group
from alien.models import Alien
from .models import ParkingProfile, ParkingBooking


class ParkingServices:

    @staticmethod
    def create_parking(
            username: str,
            email: str,
            first_name: str,
            last_name: str,
            country: str,
            city: str,
            region_name: str,
            longitude: str,
            latitude: str,
            is_available: str,
            status: str
    ) -> ParkingProfile:
        new_parking = ParkingProfile.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            country=country,
            city=city,
            region_name=region_name,
            latitude=latitude,
            longitude=longitude,
            is_available=is_available,
            status=status
        )
        my_group = Group.objects.create(name='Parking')
        my_group.user_set.add(new_parking)
        return new_parking


class BookingParking:

    @staticmethod
    def bookig_parking(
            alien: Alien,
            parking: ParkingProfile,
            check_in: str,
            check_out: str
    ) -> ParkingBooking:
        booking = ParkingBooking.objects.create(
            alien_id=alien,
            parking_id=parking,
            check_in=check_in,
            check_out=check_out
        )
        return booking
