from .models import Pharmacy


class PharmacyServices:

    @staticmethod
    def register_pharmacy(
            name: str,
            address: str,
            country: str,
            city: str,
            region_name: str,
            longitude: float,
            latitude: float,
            start_time: str,
            end_time: str,
            mobile_number: int
    ) -> Pharmacy:
        new_pharmacy = Pharmacy.objects.create(
            name=name,
            address=address,
            country=country,
            city=city,
            region_name=region_name,
            longitude=longitude,
            latitude=latitude,
            start_time=start_time,
            end_time=end_time,
            mobile_number=mobile_number
        )

        return new_pharmacy
