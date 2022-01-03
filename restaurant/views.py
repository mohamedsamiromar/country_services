import json
import re
from django.shortcuts import render
from rest_framework import serializers
from . serializers import ResturantSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status


class ResturantRegisterApplicationView(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ResturantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetResturantRegisterApplicationView(APIView):

    def get(self, request):
        serializer = ResturantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)