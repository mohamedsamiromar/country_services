from Tools.scripts.var_access_benchmark import A
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import ForgetPassword
import random
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
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
            user.set_password(password)
            user.save()
            return Response(RegisterSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(RegisterSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=None):
        user = User.objects.get(pk=pk)
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
        number = random.sample(range(10, 30), 2)

        strings = [str(integer) for integer in number]
        a_string = "".join(strings)
        an_integer = int(a_string)

        print(an_integer)
        if user:
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
            if forget_password.verification_code:
                forget_password.verification_code = an_integer
            else:
                forget_password.verification_code = an_integer
            forget_password.save()
            return Response({"Message": "Please Check Your Email"}, status=status.HTTP_200_OK)
        else:
            return Response({"Message": "This Email Is Not Found"}, status=status.HTTP_400_BAD_REQUEST)


class VerificationCodeView(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=id):
        user = ForgetPassword.objects.get(user=pk)
        code = request.GET.get('verification_code')
        if user:
            if code == user.verification_code:
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response({"Message": "This Code Is Expired"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message": "THis User Is Not Found"}, status=status.HTTP_400_BAD_REQUEST)


class NewPassword(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=id):
        user = User.objects.get(pk=pk)
        new_password = request.GET.get('new password ')
        if user:
            user.password = new_password
            user.save()
            return Response({"Message": "Your Password Is Chaged"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message": "THis User Is Not Found"}, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginCallback(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token = Token.objects.create(user=request.user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class Test(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'message': 'welcome'})

