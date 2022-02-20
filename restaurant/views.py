from pip._internal import self_outdated_check
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .serializers import ResturantRegisterApplicationserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from .serializers import MenuSerializer
from . services import ResturanServices


class ResturantRegisterApplicationView(APIView):
    serializer = ResturantRegisterApplicationserializer()

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ResturantRegisterApplicationserializer(data=data)
        serializer.is_valid(raise_exception=True)
        # instance = ResturanServices.register_resturant(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MenuView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
