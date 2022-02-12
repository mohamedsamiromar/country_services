from http import server
from rest_framework import serializers
from location.serializers import CurrentLocationSerializer


# this serializer related creations and any updates 
class ALienRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    residence = Residence()
    country = serializers.CharField()


class ResidenceSerializer(serializers.Serializer):
    location = CurrentLocationSerializer()