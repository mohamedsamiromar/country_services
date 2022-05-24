from rest_framework import serializers

class ParkProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    mobile_number = serializers.IntegerField()
    country = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()