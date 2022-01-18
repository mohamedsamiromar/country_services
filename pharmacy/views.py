from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from autoui.pagination import BasicPagination
from .queries import list_pharmacy
from .serializer import pharmacySerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class PharmacyView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer = pharmacySerializer
    pagination_class = BasicPagination


    def create(self, request):
        data = JSONParser().parse(request)
        self.serializer(data=data)
        if self.serializer.is_valid():
            self.serializer.save()
            return Response(self.serializer.data)
        else:
            return Response(self.serializer.errors)

    def list(self, request):
        query_set = list_pharmacy()
        page = self.paginate_queryset(query_set)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer(page, many=True).data)
        else:
            serializer = self.serializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)