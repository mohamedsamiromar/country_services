"""autoui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

from authentication.facebook import get_facebook_url
from authentication.google import get_google_url
from authentication.views import VerifyEmail, ConfirmEmail, ForgetPasswordView, VerificationCodeView, NewPassword, \
    RegisterView, GoogleLoginCallback, Test
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # all auth
    path('auth/', include('rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),

    # path('auth/registration/', include('rest_auth.registration.urls')),
    path('login', views.obtain_auth_token, name='api_token_auth'),
    path('register', RegisterView.as_view()),

    # VerifyEmail
    path('verify-email/<int:pk>', VerifyEmail.as_view(), name='verify-email'),
    path('confirm_email/<int:pk>', ConfirmEmail.as_view(), name='confirm_email'),

    # FaceBook Signin
    path("facebook-url", get_facebook_url, name="facebook-login"  ),

    # Google SignIn
    path('google-url', get_google_url),

    # forget password
    path('forget_password/<int:pk>', ForgetPasswordView.as_view()),
    path('verification_code/<int:pk>', VerificationCodeView.as_view()),
    path('new_password/<int:pk>', NewPassword.as_view()),

    path('google/callback', GoogleLoginCallback.as_view()),
    path('test', Test.as_view()),

    path('token', obtain_auth_token, name='api_token_auth'),

]
