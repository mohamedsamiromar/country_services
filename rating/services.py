from restaurant.models import RestaurantBooking, RestaurantProfile
from rating.models import Rating
from rating import queries


class RestaurantRatingService:
    @staticmethod
    def restaurant_rating(
            rate: int,
            comment: str,
            restaurant: RestaurantProfile
    ):
        rating = Rating.objects.create(
            rate=rate,
            comment=comment
        )
        rating.save()

        rate_restaurant = queries.get_restaurant_booking(restaurant=restaurant)
        rate_restaurant.restaurant = rating.id
        rate_restaurant.save()
        return rating
