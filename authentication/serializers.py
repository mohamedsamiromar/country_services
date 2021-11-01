from rest_framework import serializers
from .models import ForgetPassword


class ForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgetPassword
        fields = ['id', 'user', 'verification_code', 'time']


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()