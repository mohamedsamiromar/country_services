from rest_framework import serializers
from .models import ParkingProfile


class ParkingSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    region_name = serializers.CharField()
    longitude = serializers.CharField()
    latitude = serializers.CharField()
    is_available = serializers.CharField()
    status = serializers.CharField()


class ListParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingProfile
        exclud = ['status']


class ParkingBookingSerializer(serializers.Serializer):
    check_in = serializers.DateTimeField()
    check_out = serializers.DateTimeField()