from django.contrib.auth.models import Group
from rest_framework import serializers

from accounts.models import CustomUser
from .models import Alien


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name',
                  'middle_name', 'last_name', 'email']


class ALienRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alien
        fields = '__all__'

    def create(self, validated_data):
        return Alien.objects.create(validated_data)
