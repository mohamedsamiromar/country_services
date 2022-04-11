from restaurant.models import RestaurantProfile, RestaurantBooking
from core.errors import Error, APIError


def get_restaurant(id: int) -> RestaurantProfile:
    try:
        return RestaurantProfile.objects.get(pk=id)
    except RestaurantProfile.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND)


def get_restaurant_booking(restaurant: RestaurantProfile):
    try:
        return RestaurantBooking.objects.get(
            restaurant=restaurant
        )
    except RestaurantBooking.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND)