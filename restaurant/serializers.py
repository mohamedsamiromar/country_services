from rest_framework import fields, serializers
from .models import ResturantRegisterApplication, Menu
from location.serializers import CurrentLocationSerializer


class ResturantRegisterApplicationserializer(serializers.ModelSerializer):
    location = CurrentLocationSerializer()

    class Meta:
        model = ResturantRegisterApplication
        fields = ['name', 'user_name', 'last_name', 'password', 'email', 'mobile_number',
                  'address', 'location', 'start_working',
                  'end_working', 'status']
        write_only_fields = ['password']

    def create(self, validated_data):
        resturant = ResturantRegisterApplication.objects.create(**validated_data)
        # instance = self.Meta.model(**validated_data)
        return resturant

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.start_working = validated_data.get('start_working', instance.start_working)
        instance.end_working = validated_data.get('end_working', instance.end_working)
        instance.status = validated_data.get('status', instance.status)
        instance.save()


class MenuSerializer(serializers.Serializer):
    sandwiches = serializers.CharField()
    meal = serializers.CharField()

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)

