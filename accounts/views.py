from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.serializer import ResetPasswordSerializer, UserSerializer, AlienTokenObtainPairSerializer, \
    ResturantEmployeeTokenObtainPairSerializer
from accounts.services import AccountService


class UserAccountView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AlienTokenObtainPairView(TokenObtainPairView):

    def post(self, request):
        serializer = AlienTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)


class ResturantTokenObtainPairView(TokenObtainPairView):

    def post(self, request):
        serializer = ResturantEmployeeTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)
