from .models import ResturantProfile


class ResturanServices:

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
    ) -> ResturantProfile:
        new_resturant = ResturantProfile(
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
        new_resturant.save()
        return new_resturant
