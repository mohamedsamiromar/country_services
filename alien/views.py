from http import server
import re
from turtle import st
from django.shortcuts import render
from rest_framework import viewsets
from . permission import AlienAccountAccess
from . serializer import ALienRegisterSerializer
from alien import services
from rest_framework.response import Response
from rest_framework import status

class RegisterAlienView(viewsets.ViewSet):

    def create(self, request):
        serializer = ALienRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = services.AlineServices(**serializer.validate)
        return Response(instance, status=status.HTTP_201_CREATED)