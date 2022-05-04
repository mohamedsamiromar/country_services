from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from accounts.serializer import ResetPasswordSerializer
from accounts.services import AccountService
from .serializer import ALienRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import AlineServices


class RegisterAlienView(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        serializer = ALienRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = AlineServices.register_alien(**serializer.validated_data)
        return Response(ALienRegisterSerializer(instance).data, status=status.HTTP_201_CREATED)


class ResetPasswordView(APIView):
    def put(self, request):
        data = JSONParser().parse(request)
        serializer = ResetPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evt = AccountService.reset_password(**serializer.validated_data)
        return Response({'message': _('Password changed successfully.')})
