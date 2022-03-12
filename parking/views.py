from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ParkingSerializer, ParkingBookingSerializer
from .services import ParkingServices, BookingParking
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from parking import queries
from rest_framework.authtoken.models import Token


class ParkingView(APIView):
    permission_classes = AllowAny

    def post(self, request, *args, **kwargs):
        serailizer = ParkingSerializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        instance = ParkingServices.create_parking(**serailizer.validated_data)
        return Response(
            ParkingSerializer(instance).data, status=status.HTTP_201_CREATED)


class BookingParkingView(APIView):
    permission_classes = IsAuthenticated

    def post(self, request, alien):
        serializer = ParkingBookingSerializer(data=request.data)
        get_alien = queries.get_alien(id=alien)
        parking = request.user.id
        get_parking = queries.get_parking(user=parking)
        serializer.is_valid(raise_exception=True)
        instance = BookingParking.bookig_parking(
            alien=get_alien,
            parking=get_parking,
            **serializer.validated_data
        )
        return Response(
            ParkingBookingSerializer(instance).data, status=status.HTTP_201_CREATED)