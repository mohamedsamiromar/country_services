from django.core.mail import EmailMessage
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from autoui.settings import base
from .models import Pharmacy


@receiver(signals.post_save, sender=Pharmacy)
def get_longitude_and_latitude_for_pharmacy(sender, instance, create, **kwargs):
    if instance:
        if create:
            template = render_to_string('templete/select_location_pharmacy.html', {"info": instance})
            email = EmailMessage(
                'Welcome in Autoui',
                template,
                base.EMAIL_HOST_USER,
                [instance.email]
            )
            email.send()
            return
