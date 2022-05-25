from rest_framework import serializers
from alien.serializer import ALienRegisterSerializer

class HotelSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    name = serializers.CharField()
    phone_number = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()


class RoomSerializer(serializers.Serializer):
    hotel = serializers.IntegerField()
    room_numbers = serializers.IntegerField()
    floor = serializers.IntegerField()


class BookingSerializer(serializers.Serializer):
    alien = serializers.IntegerField()
    hotel = serializers.CharField()
    check_in = serializers.BooleanField()
    check_out = serializers.BooleanField()
