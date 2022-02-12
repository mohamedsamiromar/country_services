from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from core.pagination import BasicPagination
from pharmacy import queries
from .serializer import pharmacySerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .services import PharmacyServices


class PharmacyView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer = pharmacySerializer
    pagination_class = BasicPagination

    def create(self, request):
        data = JSONParser().parse(request)
        self.serializer(data=data)
        instance = PharmacyServices.register_pharmacy(self.serializer.validated_data)
        return Response(self.serializer(instance).data)

    def list(self, request):
        query_set = queries.list_pharmacy()
        page = self.paginate_queryset(query_set)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer(page, many=True).data)
        else:
            serializer = self.serializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrive(self, pharm_id):
        query_set = queries.get_pharmacy_by_id(id=pharm_id)
        serializer = pharmacySerializer(query_set)
        return Response(serializer.data)
