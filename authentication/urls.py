from django.urls import path
from authentication import views as current_view
from authentication.google import get_google_url
from authentication.facebook import get_facebook_url

urlpatterns = [
    # Register
    # VerifyEmail
    path('confirm_email/<int:pk>', current_view.ConfirmEmail.as_view(), name='confirm_email'),

    # FaceBook Signin
    path("facebook-url", get_facebook_url, name="facebook-login"),

    # Google SignIn
    path('google-url', get_google_url),


    path('google/callback', current_view.google_callback_token),
]
