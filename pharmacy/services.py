from .models import Pharmacy
from django.contrib.auth.models import Group


class PharmacyServices:

    @staticmethod
    def register_pharmacy(
            first_name: str,
            last_name: str,
            username: str,
            password: str,
            email: str,
            address: float,
            country: float,
            city: str,
            start_time: str,
            end_time: str,
            mobile_number: int
    ) -> Pharmacy:
        new_pharmacy = Pharmacy.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
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
