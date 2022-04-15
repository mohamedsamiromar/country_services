from accounts.models import GroupEnum, CustomUser
from core.errors import APIError, Error
from .models import LoginLog


class AccountService:

    @staticmethod
    def alien_optain_access_token(user: CustomUser, token: dict) -> dict:
        user = CustomUser.objects.get(pk=user.id)
        if user.is_blocked:
            raise APIError(Error.BLOCKED_USER)

        if not user.groups.filter(name=GroupEnum.ALIEN_GROUP.value):
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
        token['roles'] = list(user.groups.all().values())
        return token

    @staticmethod
    def restaurant_optain_access_token(user: CustomUser, token: dict) -> dict:
        user = CustomUser.objects.get(pk=user.id)
        if user.is_blocked:
            raise APIError(Error.BLOCKED_USER)

        if not user.groups.filter(name=GroupEnum.RESTURANT_GROUP.value):
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
        token['roles'] = list(user.groups.all().values())
        return token

    @staticmethod
    def pharmacy_optain_access_token(user: CustomUser, token: dict) -> dict:
        user = CustomUser.objects.get(pk=user.id)
        if user.is_blocked:
            raise APIError(Error.BLOCKED_USER)

        if not user.groups.filter(name=GroupEnum.PHARMACY_GROUP.value):
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
        token['roles'] = list(user.groups.all().values())
        return token


    @staticmethod
    def parking_optain_access_token(user: CustomUser, token: dict) -> dict:
        user = CustomUser.objects.get(pk=user.id)
        if user.is_blocked:
            raise APIError(Error.BLOCKED_USER)

        if not user.groups.filter(name=GroupEnum.PARKING_GROUP.value):
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
        token['roles'] = list(user.groups.all().values())
        return token

    @staticmethod
    def hotel_optain_access_token(user: CustomUser, token: dict) -> dict:
        user = CustomUser.objects.get(pk=user.id)
        if user.is_blocked:
            raise APIError(Error.BLOCKED_USER)

        if not user.groups.filter(name=GroupEnum.HOTEL_GROUP.value):
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
        token['roles'] = list(user.groups.all().values())
        return token



    @staticmethod
    def login(username: str) -> None:
        LoginLog.objects.create(username=username)
