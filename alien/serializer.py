from django.contrib.auth.models import Group
from rest_framework import serializers

from accounts.models import CustomUser
from .models import Alien


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name',
                  'middle_name', 'last_name', 'email']


class ALienRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    country = serializers.CharField()
    GENDER_CHOICES = serializers.CharField()
    gender = serializers.CharField()
    mobile_number = serializers.CharField()
    longitude = serializers.CharField()
    latitude = serializers.CharField()
    REQUIRED_FIELDS = serializers.CharField()

    def create(self, validated_data):
        return Alien.objects.create(validated_data)
