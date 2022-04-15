from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rating import queries
from rating.services import RestaurantRatingService
from rating.serializer import RestaurantRateSerializer
from rest_framework.response import Response
from rest_framework import status
from alien.permission import AlienPermission


class RestaurantRateView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, AlienPermission]

    def create(self, request):
        restaurant_id = request.GET.get('restaurant_id')
        serializer = RestaurantRateSerializer(data=request.data)
        get_restaurant = queries.get_restaurant(id=restaurant_id)
        instance = RestaurantRatingService.restauran_rating(
            restaurant=get_restaurant, **serializer.validated_data
        )
        return Response(RestaurantRateSerializer(instance).data, status=status.HTTP_201_CREATED)
