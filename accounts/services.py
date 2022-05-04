from django.contrib.auth import password_validation

from accounts.models import GroupEnum, CustomUser
from alien import queries
from core.errors import APIError, Error
from restaurant.models import RestaurantProfile
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

    @staticmethod
    def reset_password(token: str, email: str, new_password: str):
        users = queries.get_users_with(email=email)
        if users.count() != 1:
            # queries.get_users_with returns list of users, but in this case, it should return only one
            # If it does not return one user, either there is duplicate users with same email
            # or the email has no user, which should not happen because we validated
            # that when we sent the confirmation email
            raise APIError(Error.DEFAULT_ERROR)
        user = users.first()
        password_validation.validate_password(new_password, user)
        user.set_password(new_password)
        user.is_active = True
        user.save()
        return user
