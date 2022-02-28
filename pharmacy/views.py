from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from core.pagination import BasicPagination, PaginationHandlerMixin
from pharmacy import queries
from .serializer import pharmacySerializer, ListPharmacySerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .services import PharmacyServices


class PharmacyView(viewsets.ViewSet, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def create(self, request):
        serializer= pharmacySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = PharmacyServices.register_pharmacy(**serializer.validated_data)
        return Response(pharmacySerializer(instance).data)

    def list(self, request):
        query_set = queries.list_pharmacy()
        serializer = ListPharmacySerializer()
        page = self.paginate_queryset(query_set)
        if page is not None:
            serializer = self.get_paginated_response(serializer.data)
        else:
            serializer = ListPharmacySerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrive(self, pharm_id):
        query_set = queries.get_pharmacy_by_id(id=pharm_id)
        serializer = ListPharmacySerializer(query_set)
        return Response(serializer.data)
