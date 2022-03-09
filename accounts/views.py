from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions
from core.errors import APIError, Error
from accounts.models import CustomUser
from accounts.serializer import ResetPasswordSerializer, UserSerializer, AlienTokenObtainPairSerializer, \
    ResturantEmployeeTokenObtainPairSerializer
from accounts.services import AccountService
from core.utils import generate_access_token, generate_refresh_token
from alien.models import Alien
from accounts import queries

class UserAccountView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AlienTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')
        response = Response()
        if username is None or password is None:
            raise exceptions.AuthenticationFailed(Error.USER_NOT_FOUND)

        user = queries.get_username(username=username)
        alien = queries.get_alien_with(id=user)
        if user is None:
            raise exceptions.AuthenticationFailed(Error.USER_NOT_FOUND)
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed(Error.WORNG_PASSWORD)

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
        response.data = {
            'refresh_token': refresh_token,
            'access_token': access_token,
            'user': user.id,
            'role': alien    # ToDo must to change it, to return the role(group) not user
        }

        return response


class ResturantTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = ResturantEmployeeTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)
