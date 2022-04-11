from rest_framework import serializers
from core.errors import Error, APIError


class RestaurantRateSerializer(serializers.Serializer):
    rate = serializers.IntegerField()
    comment = serializers.CharField()

    def validate(self, data):
        rate = data.get['rate']
        comment = data.get['comment']

        try:
            int(rate)
        except BaseException:
            raise serializers.ValidationError(Error.INVALID_RATE)

        if comment is None:
            raise serializers.ValidationError(Error.DATA_IS_MISSING)

        return super().validate(data)
