from rest_framework import serializers
from django.contrib.auth.models import Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import CustomUser, GroupEnum
from accounts.services import AccountService


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = CustomUser
        exclude = ['password']


class AlienTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.optain_access_token(
            user=user,
            group=GroupEnum.ALIEN_GROUP,
            token=token
        )


class ServicesEmployeeTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.optain_access_token(
            user=user,
            group=GroupEnum.SERVICE_GROUP,
            token=token
        )
