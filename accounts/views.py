from allauth.account.utils import user_email
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
        if (username is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                'username and password required')

        user = Alien.objects.filter(username=username).first()
        if user is None:
            raise exceptions.AuthenticationFailed('user not found')

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
        response.data = {
            'refresh_token': refresh_token,
            'access_token': access_token,
        }

        return response


class ResturantTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = ResturantEmployeeTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)
