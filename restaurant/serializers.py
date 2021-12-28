from rest_framework import fields, serializers
from . models import ResturantRegisterApplication




class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResturantRegisterApplication
        fields = '__all__'
