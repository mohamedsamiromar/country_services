from django.core.mail import EmailMessage
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from social_core.pipeline import user

from accounts.models import CustomUser
from autoui import settings
from autoui.settings import base
from .models import Alien


@receiver(signals.post_save, sender=Alien)
def welcome_alien(sender, instance, create, **kwargs):
    if instance:
        if create:
            template = render_to_string('templete/welcome_alien.html', {'code_number':  instance})
            email = EmailMessage(
                'VerificationCode',
                template,
                base.EMAIL_HOST_USER,
                [instance.email]).send()


@receiver(signals.post_save, sender=Alien)
def create_profile(sender, instance, created, **kwargs):

    if instance:
        try:
            current_user = Alien.objects.get(
                username=instance.id)
        except CustomUser.DoesNotExist:
            new_user = CustomUser(
                email=instance.email,
                username=instance.mobile_number,
                first_name=instance.first_name,
                last_name=instance.last_name,
                middle_name=instance.middel_name,
                password=instance.password,
                is_active=False,
                preferred_lang=instance.preferred_lang
            )
            new_user.save()