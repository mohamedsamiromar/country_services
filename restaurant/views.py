from rest_framework.permissions import AllowAny

from .serializers import ResturantRegisterApplicationserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status


class ResturantRegisterApplicationView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ResturantRegisterApplicationserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
