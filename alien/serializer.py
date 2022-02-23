from rest_framework import serializers

from core.errors import Error
from location.serializers import CurrentLocationSerializer


class ALienRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    mobile_number = serializers.CharField()
    longitude = serializers.CharField()
    latitude = serializers.CharField()
    country = serializers.CharField()
