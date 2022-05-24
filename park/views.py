from rest_framework import viewsets
from park.serializer import ParkProfileSerializer
from park.services import ParkService
from rest_framework.response import Response
from rest_framework import status


class ParkRegisterView(viewsets.ViewSet):
    def create(self, request):
        serializer = ParkProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = ParkService.create_park(**serializer.validated_data)
        return Response(serializer(instance).data, status=status.HTTP_201_CREATED)