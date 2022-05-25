import re
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from park import serializer
from .serializers import HotelSerializer, BookingSerializer
from .services import HotelServices, BookingService
from rest_framework.response import Response
from rest_framework import status
from hotel import queries

class HotelView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True):
        instance = HotelServices.create_hotel(
            **serializer.validated_data
        )
        return Response(HotelSerializer(instance).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        pass

class BookingView(APIView):
    def post(self, request):
        alien = queries.get_alien(id=request.user.id)
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = BookingService.booking(alien=alien, **serializer.validated_data)
        return Response(
            BookingSerializer(instance).data, status=status.HTTP_201_CREATED
        )
