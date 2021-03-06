from django.contrib.auth.models import Group
from accounts.models import CustomUser
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
        parking_user = CustomUser.objects.create(
            email=email, username=username, first_name=first_name, last_name=last_name, password=123123)

        new_parking = ParkingProfile.objects.create(
            user=parking_user.id,
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
    def booking_parking(
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


class ParkingStatus:
    @staticmethod
    def parking_status(
            parking: ParkingProfile,
    ) -> ParkingProfile:
        pass
