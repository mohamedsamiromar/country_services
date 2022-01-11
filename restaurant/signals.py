from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.db.models import signals
from django.template.loader import render_to_string
from autoui.settings import base

from .models import ResturantRegisterApplication, ResturanProfile


@receiver(signals.post_save, sender=ResturantRegisterApplication)
def send_email_resturant_app(sender, instance, created, **kwargs):
    if instance.status == 201:
        template = render_to_string('templete/send_approved_email.html')
        email = EmailMessage(
            'Resturant Approvd',
            template,
            base.EMAIL_HOST_USER,
            [instance.email])
        email.send()


@receiver(signals.post_save, sender=ResturantRegisterApplication)
def create_resturant_profile(sender, instance, created, **kwargs):
    if instance.status == 201:
        if created:
            resturant_profile = ResturanProfile(
                name=instance.name,
                address=instance.address,
                email=instance.email,
                city=instance.city,
                country=instance.coutry
            )
        resturant_profile.save()
