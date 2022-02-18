from abc import ABC
from http import server
from rest_framework import serializers

from core.errors import Error
from location.serializers import CurrentLocationSerializer


class ALienRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    residence = CurrentLocationSerializer()
    country = serializers.CharField()

    def validators(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        residence = data.get('residence')
        country = data.get('country')

        try:
            first_name is False
        except BaseException:
            raise serializers.ValidationError(Error.DATA_IS_MISSING)

        try:
            last_name is False
        except BaseException:
            raise serializers.ValidationError(Error.DATA_IS_MISSING)

        try:
            residence is False
        except BaseException:
            raise serializers.ValidationError(Error.DATA_IS_MISSING)

        try:
            country is False
        except BaseException:
            raise serializers.ValidationError(Error.DATA_IS_MISSING)