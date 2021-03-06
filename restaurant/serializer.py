from rest_framework import fields, serializers
from .models import Menu, RestaurantProfile


class ResturantRegisterApplicationserializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    name = serializers.CharField()
    mobile_number = serializers.CharField()

    sandwiches = serializers.CharField()
    meal = serializers.CharField()
    
    address = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    start_working = serializers.CharField()
    end_working = serializers.CharField()
    occupied_table = serializers.CharField()
    available_table = serializers.CharField()
    def create(self, validated_data):
        return RestaurantProfile.objects.create(**validated_data)


class MenuSerializer(serializers.Serializer):
    sandwiches = serializers.CharField()
    meal = serializers.CharField()

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)
