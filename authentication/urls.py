from django.urls import path
from authentication import views as current_view
from authentication.google import get_google_url
from authentication.facebook import get_facebook_url
from .views import RegisterView

urlpatterns = [
    # Register
    path('register', RegisterView.as_view(), name='register'),
    # VerifyEmail
    path('verify-email/<int:pk>', current_view.VerifyEmail.as_view(), name='verify-email'),
    path('confirm_email/<int:pk>', current_view.ConfirmEmail.as_view(), name='confirm_email'),

    # FaceBook Signin
    path("facebook-url", get_facebook_url, name="facebook-login"),

    # Google SignIn
    path('google-url', get_google_url),

    # forget password
    path('forget_password/<int:pk>', current_view.ForgetPasswordView.as_view()),
    path('verification_code/<int:pk>', current_view.verification_code_view),
    path('new_password/<int:pk>', current_view.NewPassword.as_view()),

    path('google/callback', current_view.google_callback_token),
]

# mysql -u {{your_user_name}} -p{{yourpassworkd}}

# CREATE SCHEMA autoui

# mysql -h {localhost} -u username -p {root}
