import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token


class ConfirmEmail(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=id):
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return Response({"Message": "Your email is verified, Thanks"}, status=status.HTTP_201_CREATED)


#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         token = Token.objects.get_or_create(user=request.user)
#         content = {'token': token[0].key}
#         return HttpResponse(json.dumps(content), content_type="application/json")
# #
#
# class Test(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         return Response({'message': 'welcome'})
#
#
# class GoogleLoginCallback(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         token = Token.objects.create(user=request.user)
#         return Response({'token': token.key}, status=status.HTTP_200_OK)
#


def google_callback_token(request):
    token = Token.objects.get_or_create(user=request.user)
    content = {'token': token[0].key}
    return HttpResponse(json.dumps(content), content_type="application/json")
