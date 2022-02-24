from rest_framework import serializers

from accounts.models import CustomUser
from core.errors import Error
from location.serializers import CurrentLocationSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name',
                  'middle_name', 'last_name', 'email']


class ALienRegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    mobile_number = serializers.CharField()
    longitude = serializers.CharField()
    latitude = serializers.CharField()
    country = serializers.CharField()
