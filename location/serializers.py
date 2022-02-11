from rest_framework import serializers
from .models import CurrentLocation


class CurrentLocationSerializer(serializers.Serializer):
    region_name = serializers.CharField()
    longitude = serializers.CharField()
    latitude = serializers.CharField()