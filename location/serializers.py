from rest_framework import serializers
from . models import CurrentLocation


class CurrentLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLocation
        fileds = ['id', 'user', 'country', 'city', 'region_name']