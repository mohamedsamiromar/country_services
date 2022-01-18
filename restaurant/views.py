from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .serializers import ResturantRegisterApplicationserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets
from .serializers import MenuSerializer


class ResturantRegisterApplicationView(APIView):
    permission_classes = [AllowAny, ]
    serializer = ResturantRegisterApplicationserializer()

    def post(self, request):
        data = JSONParser().parse(request)
        self.serializer(data=data)
        if self.serializer.is_valid():
            self.serializer.save()
            return Response(self.serializer.data)
        else:
            return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
