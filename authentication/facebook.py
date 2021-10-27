from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
import os


FACEBOOK_DEBUG_TOKEN_URL = "https://graph.facebook.com/debug_token"
FACEBOOK_ACCESS_TOKEN_URL = "https://graph.facebook.com/v7.0/oauth/access_token"
FACEBOOK_URL = "https://graph.facebook.com/"


class SignInView(APIView):
    def get(self, request):
        user_access_token_payload = {
            "client_id": os.environ.get("FACEBOOK_APP_ID"),
            "redirect_uri": "http://localhost:8000/login/",
            "client_secret": os.environ.get("FACEBOOK_APP_SECRET"),
            "code": request.query_params.get("code"),
        }
        user_access_token_request = requests.get(
            FACEBOOK_ACCESS_TOKEN_URL, params=user_access_token_payload
        )
        user_access_token_response = json.loads(user_access_token_request.text)
        if "error" in user_access_token_response:
            user_access_token_error = {
                "message": "wrong facebook access token / this facebook access token is already expired."
            }
            return Response(user_access_token_error)

        user_access_token = user_access_token_response["access_token"]

        developers_access_token_payload = {
            "client_id": os.environ.get("FACEBOOK_APP_ID"),
            "client_secret": os.environ.get("FACEBOOK_APP_SECRET"),
            "grant_type": "client_credentials",
        }
        developers_access_token_request = requests.get(
            FACEBOOK_ACCESS_TOKEN_URL, params=developers_access_token_payload
        )
        developers_access_token_response = json.loads(
            developers_access_token_request.text
        )

        if "error" in developers_access_token_response:
            developers_access_token_error = {
                "message": "Invalid request for access token."
            }
            return Response(developers_access_token_error)

        developers_access_token = developers_access_token_response["access_token"]

        verify_user_access_token_payload = {
            "input_token": user_access_token,
            "access_token": developers_access_token,
        }

        verify_user_access_token_request = requests.get(
            FACEBOOK_DEBUG_TOKEN_URL, params=verify_user_access_token_payload
        )
        verify_user_access_token_response = json.loads(
            verify_user_access_token_request.text
        )

        if "error" in verify_user_access_token_response:
            verify_user_access_token_error = {
                "message": "Could not verifying user access token."
            }
            return Response(verify_user_access_token_error)

        user_id = verify_user_access_token_response["data"]["user_id"]

        user_info_url = FACEBOOK_URL + user_id
        user_info_payload = {
            "fields": "id,name,email",
            "access_token": user_access_token,
        }

        user_info_request = requests.get(user_info_url, params=user_info_payload)
        user_info_response = json.loads(user_info_request.text)

        users_email = user_info_response["email"]

        # create user if not exist
        try:
            user = User.objects.get(email=user_info_response["email"])
        except User.DoesNotExist:
            user = User()
            user.username = user_info_response["email"]
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = user_info_response["email"]
            user.save()

        token = RefreshToken.for_user(
            user
        )  # generate token without username & password
        response = {"username": user.username, "access_token": str(token.access_token), "refresh_token": str(token)}
        return Response(response)