from restaurant.models import RestaurantBooking, RestaurantProfile
from rating.models import Rating
from rating import queries


class RestaurantRatingService:
    @staticmethod
    def restauran_rating(
            rate: int,
            comment: str,
            restaurant: RestaurantProfile
    ):
        rating = Rating.objects.create(
            rate=rate,
            comment=comment
        )
        rating.save()

        rate_resturant = queries.get_restaurant_booking(restaurant=restaurant)
        rate_resturant.restaurant = rating.id
        rate_resturant.save()
        return rating
