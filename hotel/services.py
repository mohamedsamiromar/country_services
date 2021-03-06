from datetime import datetime
from hotel import queries
from accounts.models import CustomUser
from .models import Booking, Hotel, Room
from django.contrib.auth.models import Group
from alien.models import Alien

class HotelServices:

    @staticmethod
    def create_hotel(
            username: str,
            first_name: str,
            last_name: str,
            email: str,
            name: str,
            country: str,
            city: str,
            phone_number: int,
    ) -> Hotel:
        hotel_user = CustomUser.objects.create(
            email=email, username=username, first_name=first_name, last_name=last_name, password=123123)
        hotel = Hotel(
            user=hotel_user.id,
            name=name,
            country=country,
            city=city,
            phone_number=phone_number
        )
        hotel.save()
        my_group = Group.objects.create(name='Hotel')
        my_group.user_set.add(hotel)
        return hotel

    @staticmethod
    def room_services(
            hotel: Hotel,
            rooms_number: int,
            floor: int,
    ) -> Room:
        room = Room(
            hotel=hotel,
            rooms_number=rooms_number,
            floor=floor
        )
        room.save()
        return room

class BookingService:
    @staticmethod
    def booking(
        alien: Alien,
        hotel: Hotel,
        room: Room,
        check_in: datetime,
        check_out: datetime
    ) -> Booking:
        hotel = queries.get_hotel(id=hotel)
        booking = Booking.objects.create(
            alien= alien, hotel=hotel, room=room, check_in=check_in, check_out=check_out
        )
        return booking