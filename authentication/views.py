import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ForgetPassword
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            frist_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = User()
            user.first_name = frist_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.password = password
            user.save()
            return Response(RegisterSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(RegisterSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmEmail(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=id):
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return Response({"Message": "Your email is verified, Thanks"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def verification_code_view(request, pk=id):
    user = ForgetPassword.objects.get(pk=pk)
    code = request.POST.get('verification_code')
    if user.verification_code == int(code):
        return Response("Code is True", status=status.HTTP_201_CREATED)
    else:
        return Response("Invalid Code", status=status.HTTP_400_BAD_REQUEST)


# class GoogleLoginCallback(APIView):
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
