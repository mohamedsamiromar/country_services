from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import generics
from auth_api.serializer import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import ForgetPassword
import random


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(RegisterSerializer(user).data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):

    def get(self, request, pk=id):
        user = User.objects.get(pk=pk)
        if user:
            if user.is_active:
                return Response({"Message": "Your Email Is Verify"})
            else:
                template = render_to_string('send_email.html')
                email = EmailMessage(
                    'VerifyEmail',
                    template,
                    settings.EMAIL_HOST_USER,
                    [user.email])
            email.send()

        else:
            return Response({"Message": "This User Is Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message": "Email Is Sent"}, status=status.HTTP_201_CREATED)


class ConfirmEmail(generics.GenericAPIView):
    def get(self, request, pk=id):
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return Response({"Message": "Your email is verified, Thanks"}, status=status.HTTP_201_CREATED)


class ForgetPasswordView(generics.GenericAPIView):
    def Post(self, request, pk=id):
        user = User.objects.get(pk=pk)
        number = random.sample(range(10, 30), 4)
        if user:
            email = EmailMessage(
                'Forget Password',
                number,
                settings.EMAIL_HOST_USER,
                [user.email])
            email.send()
            forget_password = ForgetPassword()
            forget_password.time = now()
            forget_password.user = user
            forget_password.verification_code = number
            forget_password.save()
            return Response({"Message": "Please Check Your Email"}, status=status.HTTP_200_OK)
        else:
            return Response({"Message": "This Email Is Not Found"}, status=status.HTTP_400_BAD_REQUEST)


class VerificationCodeView(generics.GenericAPIView):
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
    def get(self, request, pk=id):
        user = User.objects.get(pk=pk)
        new_password = request.GET.get('new password ')
        if user:
            user.password = new_password
            user.save()
            return Response({"Message": "Your Password Is Chaged"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message": "THis User Is Not Found"}, status=status.HTTP_400_BAD_REQUEST)