import logging
from django.core.mail import send_mail
from django.template.loader import render_to_string
from autoui.celery import app
from accounts.models import CustomUser
from core.conf import Configuration as Conf
from django.conf import settings
from core.utils import generate_token


@app.task
def send_verification_email(user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        token = generate_token(user.id)
        template = render_to_string('verification_code.html', {"name": user.first_name, "reset_password_link": f'{Conf.WEBSITE_URL()}/auth/reset-password/{token}'})
        email = send_mail(
            'VerifyEmail',
            template,
            settings.EMAIL_HOST_USER,
            [user.email])
        email.send()
    except CustomUser.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
