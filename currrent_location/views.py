import json
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CurrentLocation, GetLocationManual
from currrent_location.serializers import CurrentLocationSerializer,CurrentLocationManualSerializer



@api_view(['GET'])
@permission_classes([AllowAny])
def get_current_location(request):
    serializer = CurrentLocationSerializer(data=request.data)
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    re = requests.get('http://ip-api.com/json/' + ip_data['ip'])
    location_data_one = re.text
    location_data = json.loads(location_data_one)
    city = location_data.get('city')
    country = location_data.get('country')
    region_name = location_data.get('regionName')
    latitude = location_data.get('lat')
    longitude = location_data.get('lon')
    if serializer.is_valid():
        current_location = CurrentLocation()
        user = request.GET.get('user')
        current_location.User = user
        current_location.city = city
        current_location.country = country
        current_location.region_name = region_name
        current_location.longitude = longitude
        current_location.latitude = latitude
        current_location.save()

        return Response(CurrentLocationSerializer(current_location).data, status=status.HTTP_200_OK)
    return Response(CurrentLocationSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_current_location_manual(request):
    if request.method == 'GET':
        location = GetLocationManual.objects.all()
        serializer = CurrentLocationManualSerializer(location, many=True)
        return Response(serializer.data)