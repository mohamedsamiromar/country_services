from rest_framework import fields, serializers
from .models import ResturantRegisterApplication, Menu
from location.serializers import CurrentLocationSerializer


class ResturantRegisterApplicationserializer(serializers.Serializer):
    name = serializers.CharField()
    user_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.CharField()
    mobile_number = serializers.CharField()
    address = serializers.CharField()
    location = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    start_working = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    end_working = serializers.CharField()


class MenuSerializer(serializers.Serializer):
    sandwiches = serializers.CharField()
    meal = serializers.CharField()

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)
