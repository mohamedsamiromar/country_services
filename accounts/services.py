from accounts.models import GroupEnum, CustomUser
from core.errors import APIError, Error
from restaurant.models import ResturantProfile
from .models import LoginLog


class AccountService:

    @staticmethod
    def optain_alien_access_token(user: CustomUser, token: dict) -> dict:
        if not user.groups.filter(name=GroupEnum.ADMIN_GROUP.value).exists():
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
        token['roles'] = list(user.groups.all().values())
        return token

    @staticmethod
    def optain_resturant_acces_token(user: CustomUser, token: dict) -> dict:
        if not user.groups.filter(name=GroupEnum.RESTURANT_GROUP.value).exists():
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
        try:
            token['roles'] = list(user.groups.all().values())
            return token
        except ResturantProfile.DoesNotExist:
            raise APIError(Error.NO_ACTIVE_ACCOUNT)

    @staticmethod
    def optain_access_token(group: GroupEnum, user: CustomUser, token: dict) -> dict:

        if group == GroupEnum.ADMIN_GROUP:
            return AccountService.optain_alien_access_token(
                user=user, token=token)
        elif group == GroupEnum.ALIEN_GROUP:
            return AccountService.optain_resturant_acces_token(
                user=user, token=token)
        elif group == GroupEnum.RESTURANT_GROUP:
            return AccountService.optain_resturant_acces_token(
                user=user, token=token)
        else:
            raise APIError(Error.NO_ACTIVE_ACCOUNT)

    @staticmethod
    def login(username: str) -> None:
        LoginLog.objects.create(username=username)
