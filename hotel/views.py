from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import HotelSerializer
from .services import HotelServices
from rest_framework.response import Response
from rest_framework import status


class HotelView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = HotelServices.create_hotel(
                **serializer.validated_data
            )
            return Response(HotelSerializer(instance).data, status=status.HTTP_201_CREATED)


# ToDo
'''
- Send email once the hotel approved
'''
