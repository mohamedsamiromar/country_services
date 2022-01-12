import json

import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import CurrentLocation
from location.serializers import CurrentLocationSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_current_location(request):
    serializer = CurrentLocationSerializer(data=request.data)
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    re = requests.get('http://ip-api.com/json/' + ip_data['ip'])
    return Response(re, status=status.HTTP_200_OK)
    location_data_one = re.text
    location_data = json.loads(location_data_one)
    city = location_data.get('city')
    country = location_data.get('country')
    region_name = location_data.get('regionName')
    longitude = location_data.get('longitude')
    latitude = location_data.get('latitude')
    if serializer.is_valid():
        city = serializer.validated_data['city']
        country = serializer.validated_data['country']
        region_name = serializer.validated_data['region_name']
        longitude = serializer.validated_data['longitude']
        latitude = serializer.validated_data['latitude']
        serializer.save()
        return Response(CurrentLocationSerializer(current_location).data, status=status.HTTP_200_OK)
    return Response(CurrentLocationSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# python manage.py --settings=autoui.settings runserver/syncdb
# python manage.py runserver --settings=autoui.settings.dev


# (venv) root@ubuntu-s-1vcpu-2gb-intel-ams3-01:~/autour-backend# python manage.py runserver 0.0.0.0:8000
