import json
import requests
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CurrentLocation, GetLocationManual, SelecteCountryAndCity
from currrent_location.serializers import CurrentLocationSerializer, CurrentLocationManualSerializer, \
    SelecteCountryAndCitySerializer
from .pagination import LargeResultsSetPagination, StandardResultsSetPagination

'''
 get_current_location 
 If the user will allow the GPS location
 that will get user city, country, region_name, longitude and latitude
 and then save that in the table CurrentLocation()
'''


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
        current_user = request.user
        current_location.city = city
        current_location.country = country
        current_location.region_name = region_name
        current_location.longitude = longitude
        current_location.latitude = latitude
        current_location.save()

        return Response(CurrentLocationSerializer(current_location).data, status=status.HTTP_200_OK)
    return Response(CurrentLocationSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
if user doesn't allowed the GPS,here we will display countries and cities and the user can selet his own country 
and city, countries with cities, the countries and cities created by admin model
'''


class GetCurrentLocationaManualy(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = GetLocationManual.objects.all()
    serializer_class = CurrentLocationManualSerializer
    pagination_class = LargeResultsSetPagination


'''
here will send id GetLocationManual in url the user chose, and save that
'''


@api_view(['GET'])
@permission_classes([AllowAny])
def select_country_city_view(request, pk=None):
    serializer = SelecteCountryAndCitySerializer(data=request.data)
    location = GetLocationManual.objects.get(pk=pk)
    if serializer.is_valid():
        select_country_city = SelecteCountryAndCity()
        select_country_city.User = request.user
        select_country_city.country = location.country
        select_country_city.city = location.city
        select_country_city.save()
        return Response(SelecteCountryAndCitySerializer(select_country_city).data, status=status.HTTP_201_CREATED)
    return Response(SelecteCountryAndCitySerializer.errors, status=status.HTTP_201_CREATED)

# python manage.py --settings=autoui.settings runserver/syncdb
# python manage.py runserver --settings=autoui.settings.dev
