from . models import ResturantRegisterApplication


class ResturanServices:

    @staticmethod
    def register_resturant(
            name: str,
            user_name: str,
            last_name : str,
            password: str,
            mobile_number: int,
            address : str,
            location: str,
            start_working: str,
            end_working: str,
            status: int,
    ) -> ResturantRegisterApplication:
        new_resturant = ResturantRegisterApplication.objects.create(
            name=name,
            user_name=user_name,
            last_name=last_name,
            password=password,
            mobile_number=mobile_number,
            address=address,
            location=location,
            start_working=start_working,
            end_working=end_working,
            status=status
        )
        return new_resturant