from .models import RestaurantProfile
from django.contrib.auth.models import Group


class RestaurantServices:

    @staticmethod
    def register_resturant(
            name: str,
            mobile_number: str,
            address: str,
            email: str,
            country: str,
            city: str,
            start_working: str,
            end_working: str,
            occupied_table: str,
            available_table: str
    ) -> RestaurantProfile:
        new_restaurant = RestaurantProfile(
            name=name,
            mobile_number=mobile_number,
            address=address,
            email=email,
            country=country,
            city=city,
            start_working=start_working,
            end_working=end_working,
            occupied_table=occupied_table,
            available_table=available_table,
        )
        new_restaurant.save()
        my_group = Group.objects.create(name='Restaurant')
        my_group.user_set.add(new_restaurant)
        my_group.save()
