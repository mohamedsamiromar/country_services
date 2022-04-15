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
        return AccountService.alien_optain_access_token(
            user=user,
            token=token
        )


class RestaurantTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.restaurant_optain_access_token(
            user=user,
            token=token
        )


class PharmacyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.pharmacy_optain_access_token(
            user=user,
            token=token
        )


class ParkingTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.parking_optain_access_token(
            user=user,
            token=token
        )


class HotelTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.hotel_optain_access_token(
            user=user,
            token=token
        )

class RequestOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(write_only=True, required=True)
