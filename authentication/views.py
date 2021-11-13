import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.timezone import now
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import ForgetPassword
import random
from rest_framework.views import APIView
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


class VerifyEmail(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=None):
        if pk is None:
            return Response({"message": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(pk=pk)
        if user is None:
            return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        if user:
            if user.is_active:
                return Response({"Message": "Your Email Is Verify"})
            else:
                template = render_to_string('send_email.html', {"name": user.first_name, "user_id": user.id})
                email = EmailMessage(
                    'VerifyEmail',
                    template,
                    settings.EMAIL_HOST_USER,
                    [user.email])
            email.send()

        else:
            return Response({"Message": "This User Is Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message": "Email Is Sent"}, status=status.HTTP_201_CREATED)


class ConfirmEmail(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=id):
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return Response({"Message": "Your email is verified, Thanks"}, status=status.HTTP_201_CREATED)


class ForgetPasswordView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=id):
        user = User.objects.get(pk=pk)
        current_user = ForgetPassword.objects.get(user=user)
        if current_user:
            number = random.sample(range(10, 30), 2)
            strings = [str(integer) for integer in number]
            a_string = "".join(strings)
            an_integer = int(a_string)
            template = render_to_string('verification_code.html', {'code_number': an_integer})
            email = EmailMessage(
                'VerificationCode',
                template,
                settings.EMAIL_HOST_USER,
                [current_user.user.email]).send()
            current_user.verification_code = an_integer
            current_user.time = now()
            current_user.save()
            return Response("Please, Check Yuor Eamil")
        else:
            number = random.sample(range(10, 30), 2)
            strings = [str(integer) for integer in number]
            a_string = "".join(strings)
            an_integer = int(a_string)
            template = render_to_string('verification_code.html', {'code_number': an_integer})
            email = EmailMessage(
                'VerificationCode',
                template,
                settings.EMAIL_HOST_USER,
                [user.email]).send()
            forget_password = ForgetPassword()
            forget_password.time = now()
            forget_password.user = user
            forget_password.verification_code = an_integer
            forget_password.save()

        return Response({"Message": "Please Check Your Email"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def verification_code_view(request, pk=id):
    user = ForgetPassword.objects.get(pk=pk)
    code = request.POST.get('verification_code')
    if user.verification_code == int(code):
        print("True")
        return Response("Code is True", status=status.HTTP_201_CREATED)
    else:
        print("False")
        return Response("Invalid Code", status=status.HTTP_400_BAD_REQUEST)


class NewPassword(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, pk=id):
        user = User.objects.get(pk=pk)
        new_password = request.POST.get('new_password')
        if new_password is None:
            return Response("Please, Enter You New Password", status=status.HTTP_400_BAD_REQUEST)
        if user:
            user.password = new_password
            print(user.password)
            user.save()
            print(user.password)
            if user.password == new_password:
                return Response({"Message": "Your Password Is Chaged"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message": "THis User Is Not Found"}, status=status.HTTP_400_BAD_REQUEST)


# class GoogleLoginCallback(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         token = Token.objects.get_or_create(user=request.user)
#         content = {'token': token[0].key}
#         return HttpResponse(json.dumps(content), content_type="application/json")
#

class Test(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'message': 'welcome'})


class GoogleLoginCallback(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        token = Token.objects.create(user=request.user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
