from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from accounts.models import CustomUser
from autoui.settings import base
from core.utils import generate_token, generate_otp
from .models import Alien
import json


@receiver(signals.post_save, sender=Alien)
def welcome_alien(sender, instance, create, **kwargs):
    if instance:
        if create:
            template = render_to_string('templete/welcome_alien.html', {'code_number': instance})
            email = EmailMessage(
                'VerificationCode',
                template,
                base.EMAIL_HOST_USER,
                [instance.email]).send()


@receiver(signals.post_save, sender=Alien)
def create_custom_user(sender, instance, create, **kwargs):
    if create:
        new_user = CustomUser.objects.create(
            username=instance.username,
            password=12313,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email
        )
        new_user.save()
        my_group = Group.objects.create(name='Alien')
        my_group.user_set.add(new_user)
        my_group.save()


@receiver(signals.post_save, sender=Alien)
def account_activation_email(sender, instance, created, **kwargs):
    if created:
        token = generate_token(instance.user.id)
        otp = generate_otp()

        notification = EmailMessage(
            type='Email',
            template='corporates/email/account_activation.html',
            title='Welcome To Autoui',
            data=json.dumps({
                "name": instance.first_name,
                "username": instance.user.username,
                "reset_password_link": f'{Conf.WEBSITE_URL()}/auth/reset-password/{token}',
                "otp": otp,
            }),
        ).send()
        return notification
