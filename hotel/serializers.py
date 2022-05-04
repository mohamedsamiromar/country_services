from rest_framework import serializers
from core.errors import Error


class HotelSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    longitude = serializers.CharField()
    latitude = serializers.CharField()
    phone_number = serializers.IntegerField()

    def validate(self, data):
        longitude = data.get('longitude')
        latitude = data.get('latitude')

        try:
            float(longitude)
        except BaseException:
            raise serializers.ValidationError(Error.INVALID_LONGITUDE)

        try:
            float(latitude)
        except BaseException:
            raise serializers.ValidationError(Error.INVALID_LATITUDE)

        return super().validate(data)


class RoomSerializer(serializers.Serializer):
    hotel = serializers.IntegerField()
    room_numbers = serializers.IntegerField()
    floor = serializers.IntegerField()
