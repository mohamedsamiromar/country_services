from .models import RestaurantProfile
from django.contrib.auth.models import Group
from accounts.models import CustomUser


class RestaurantServices:

    @staticmethod
    def register_restaurant(
            username: str,
            first_name: str,
            last_name: str,
            email: str,
            name: str,
            mobile_number: str,
            address: str,
            country: str,
            start_working: str,
            end_working: str,
            occupied_table: str,
            available_table: str
    ) -> RestaurantProfile:
        restaurant_user = CustomUser.objects.create(
            first_name=first_name, last_name=last_name, username=username, email=email, password=123123)

        new_restaurant = RestaurantProfile(
            user=restaurant_user.id,
            name=name,
            mobile_number=mobile_number,
            address=address,
            country=country,
            start_working=start_working,
            end_working=end_working,
            occupied_table=occupied_table,
            available_table=available_table,
        )
        new_restaurant.save()
        my_group = Group.objects.create(name='Restaurant')
        my_group.user_set.add(new_restaurant)
        my_group.save()
