from rest_framework import serializers
from .models import CurrentLocation


class CurrentLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLocation
        fields = '__all__'
