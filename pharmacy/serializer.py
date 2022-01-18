from rest_framework import serializers
from .models import Pharmacy


class pharmacySerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    region_name = serializers.CharField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    mobile_number = serializers.IntegerField()

    def create(self, validated_data):
        return Pharmacy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.region_name = validated_data.get('region_name', instance.region_name)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)


class ListPharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = "__all__"
