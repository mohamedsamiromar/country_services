import json
import requests
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CurrentLocation
from currrent_location.serializers import CurrentLocationSerializer
from .pagination import LargeResultsSetPagination, StandardResultsSetPagination

'''
 get_current_location 
 If the user will allow the GPS location
 that will get user city, country, region_name, longitude and latitude
 and then save that in the table CurrentLocation()
'''


@api_view(['GET'])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def current_location_view(request):
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
    if serializer.is_valid(raise_exception=True):
        current_location = CurrentLocation()
        # current_user = request.user
        # current_location.city = serializer.validated_data['city']
        # current_location.country = serializer.validated_data['country']
        # current_location.region_name = serializer.validated_data['region_name']
        # current_location.longitude = serializer.validated_data['longitude']
        # current_location.latitude = serializer.validated_data['latitude']
        serializer.save()
        return Response(CurrentLocationSerializer(current_location).data, status=status.HTTP_200_OK)
    return Response(CurrentLocationSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


# python manage.py --settings=autoui.settings runserver/syncdb
# python manage.py runserver --settings=autoui.settings.dev


# (venv) root@ubuntu-s-1vcpu-2gb-intel-ams3-01:~/autour-backend# python manage.py runserver 0.0.0.0:8000