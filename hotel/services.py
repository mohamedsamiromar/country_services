from accounts.models import CustomUser
from .models import Hotel, Room
from django.contrib.auth.models import Group


class HotelServices:

    @staticmethod
    def create_hotel(
            username: str,
            password: str,
            first_name: str,
            last_name: str,
            email: str,
            name: str,
            longitude: str,
            latitude: str,
            phone_number: int,
    ) -> Hotel:
        hotel_user = CustomUser.objects.create(
            name=name, email=email, username=username, password=password, first_name=first_name, last_name=last_name)
        hotel = Hotel(
            user= hotel_user.id,
            name=name,
            email=email,
            longitude=longitude,
            latitude=latitude,
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
