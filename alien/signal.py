from django.core.mail import EmailMessage
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string

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
                settings.EMAIL_HOST_USER,
                [user.email]).send()
