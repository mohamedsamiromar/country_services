from django.shortcuts import render
from rest_framework.views import APIView
from parking.services import ParkingStatus
from .permission import ParkingAccess
from .serializer import ParkingSerializer, ParkingBookingSerializer
from .services import ParkingServices, BookingParking
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from parking import queries


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


class ParkingFullAndNotFull(APIView):
    permission_classes = [IsAuthenticated, ParkingAccess]

    def get(self, request):
        status = request.data.get('status')
        user_parking = request.user
        user = queries.get_parking(user=user_parking)
        instance = ParkingStatus.parking_status(parking=user, status=status)
        return Response(ParkingSerializer(instance), status=status.HTTP_201_CREATED)