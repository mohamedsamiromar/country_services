import datetime
import math
import random
from django.conf import settings
import jwt


def generate_token(user_id):
    payload = {
        "token_type": "verify",
        "exp": (datetime.now() + datetime.timedelta(hours=48)).timestamp(),
        "user_id": user_id
    }
    return jwt.encode(payload, "munjiz", algorithm="HS256")


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')

    return refresh_token


def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP
