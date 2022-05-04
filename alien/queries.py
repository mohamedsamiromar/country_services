from accounts.models import CustomUser
from typing import Iterable


def get_users_with(email: str = None, mobile_number: str = None) -> Iterable[CustomUser]:
    if email and mobile_number:
        return CustomUser.objects.filter(email=email, username=mobile_number)
    elif email and not mobile_number:
        return CustomUser.objects.filter(email=email)
    elif not email and mobile_number:
        return CustomUser.objects.filter(username=mobile_number)
    else:
        None
