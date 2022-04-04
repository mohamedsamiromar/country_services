from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .serializer import ALienRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import AlineServices
from .tasks import num_sun
from rest_framework.decorators import APIView


class RegisterAlienView(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        serializer = ALienRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = AlineServices.register_alien(**serializer.validated_data)
        return Response(ALienRegisterSerializer(instance).data, status=status.HTTP_201_CREATED)


def sum_num(request):
    num_sun(2, 2)
    return Response({"MSG": "Done"})
