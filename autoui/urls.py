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

from authentication.facebook import SignInView
from authentication.google import GoogleLogin, google_callback
from authentication.views import Register, VerifyEmail, ConfirmEmail, ForgetPasswordView, VerificationCodeView, NewPassword
from allauth.socialaccount.providers.google import views as google_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # all auth
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    # Register endpoint
    path('register-api', Register.as_view(), name='register-api'),

    # VerifyEmail
    path('verify-email/<int:pk>', VerifyEmail.as_view(), name='verify-email'),
    path('confirm_email/<int:pk>', ConfirmEmail.as_view(), name='confirm_email'),

    # FaceBook Signin
    path("facebook-login/", SignInView.as_view(), name="facebook-login"),

    # Google SignIn
    path('auth/google', GoogleLogin.as_view(), name='google_login'),
    path('auth/google/',    google_callback, name='google_callback'),
    path('auth/google/url/', google_views.oauth2_login),

    # forget password
    path('forget_password/<int:pk>', ForgetPasswordView.as_view()),
    path('verification_code/<int:pk>', VerificationCodeView.as_view()),
    path('new_password/<int:pk>', NewPassword.as_view()),

]
