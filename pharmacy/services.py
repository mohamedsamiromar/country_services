from accounts.models import CustomUser
from .models import Pharmacy
from django.contrib.auth.models import Group


class PharmacyServices:

    @staticmethod
    def register_pharmacy(
            first_name: str,
            last_name: str,
            username: str,
            email: str,
            address: float,
            country: float,
            city: str,
            start_time: str,
            end_time: str,
            mobile_number: int,

    ) -> Pharmacy:
        pharmacy_user = CustomUser.objects.create(
            email=email, username=username, first_name=first_name, last_name=last_name, password=123123)
        new_pharmacy = Pharmacy.objects.create(
            user=pharmacy_user.id,
            address=address,
            country=country,
            city=city,
            start_time=start_time,
            end_time=end_time,
            mobile_number=mobile_number
        )
        new_pharmacy.save()
        my_group = Group.objects.create(name='Pharmacy')
        my_group.user_set.add(new_pharmacy)
        return new_pharmacy
