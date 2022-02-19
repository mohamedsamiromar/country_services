from rest_framework import serializers
from location.serializers import CurrentLocationSerializer


class ALienRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    country = serializers.CharField(required=False)
    residence = serializers.CharField(required=False, allow_null=False)
    email = serializers.EmailField()
    mobile_number = serializers.CharField()

    # def validators(self, data):
    #     first_name = data.get('first_name')
    #     last_name = data.get('last_name')
    #     country = data.get('country')
    #     email = data.get('email')
    #     mobile_number = data.get('mobile_number')
    #
    #     try:
    #         first_name is False
    #     except BaseException:
    #         raise serializers.ValidationError(Error.DATA_IS_MISSING)
    #
    #     try:
    #         last_name is False
    #     except BaseException:
    #         raise serializers.ValidationError(Error.DATA_IS_MISSING)
    #
    #     try:
    #         email is False
    #     except BaseException:
    #         raise serializers.ValidationError(Error.DATA_IS_MISSING)
    #
    #     try:
    #         mobile_number is False
    #     except BaseException:
    #         raise serializers.ValidationError(Error.DATA_IS_MISSING)
    #
    # try:
    #     country is False
    # except BaseException:
    #     raise serializers.ValidationError(Error.DATA_IS_MISSING)
