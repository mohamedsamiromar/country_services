from .models import ResturantRegisterApplication


class ResturanServices:

    @staticmethod
    def register_resturant(
            name: str,
            user_name: str,
            last_name: str,
            password: str,
            email: str,
            mobile_number: str,
            address: str,
            start_working: str,
            country: str,
            city: str,
            end_working: str
    ) -> ResturantRegisterApplication:
        new_resturant = ResturantRegisterApplication.objects.create(
            name=name,
            user_name=user_name,
            last_name=last_name,
            password=password,
            email=email,
            mobile_number=mobile_number,
            address=address,
            start_working=start_working,
            country=country,
            city=city,
            end_working=end_working
        )
        return new_resturant
