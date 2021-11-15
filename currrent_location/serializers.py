from rest_framework import serializers
from .models import CurrentLocation, GetLocationManual


class CurrentLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLocation
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = GetLocationManual
        fields = ['city_1', 'city_2', 'city_3']


class CurrentLocationManualSerializer(serializers.ModelSerializer):
    # city = serializers.SerializerMethodField(read_only=True)
    city_1 = serializers.CharField(read_only=True, source="city.city_1")
    city_2 = serializers.CharField(read_only=True, source="city.city_2")
    city_3 = serializers.CharField(read_only=True, source="city.city_3")

    class Meta:
        model = GetLocationManual
        fields = ['country', 'city_1', 'city_2', 'city_3']

    def get_city_1(self, obj):
        return CitySerializer(obj.city_1).data

    def get_city_2(self, obj):
        return CitySerializer(obj.city_2).data

    def get_city_3(self, obj):
        return CitySerializer(obj.city_3).data
