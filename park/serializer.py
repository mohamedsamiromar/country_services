from rest_framework import serializers

class ParkProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    name = serializers.CharField()
    mobile_number = serializers.IntegerField()
    country = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()