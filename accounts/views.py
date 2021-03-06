from allauth.account.utils import user_email
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.serializer import UserSerializer, AlienTokenObtainPairSerializer, \
    RestaurantTokenObtainPairSerializer, PharmacyTokenObtainPairSerializer, HotelTokenObtainPairSerializer, \
    ParkingTokenObtainPairSerializer
from accounts.services import AccountService


class UserAccountView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AlienTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = AlienTokenObtainPairSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)


class ResturantTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = RestaurantTokenObtainPairSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)


class PharmacyTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = PharmacyTokenObtainPairSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)


class ParkingTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = ParkingTokenObtainPairSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)


class HotelTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = HotelTokenObtainPairSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)
