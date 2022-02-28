from django.contrib.auth.models import Group

from accounts.models import CustomUser
from django.core.mail import EmailMessage
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from autoui.settings import base
from .models import Pharmacy


@receiver(signals.post_save, sender=Pharmacy)
def get_longitude_and_latitude_for_pharmacy(sender, instance, create, **kwargs):
    if instance and instance.statusstatus == 201:
        if create:
            template = render_to_string('templete/select_location_pharmacy.html', {'info': instance})
            email = EmailMessage(
                'Welcome in Autoui',
                template,
                base.EMAIL_HOST_USER,
                [instance.email]
            )
            email.send()
            return


@receiver(signals.post_save, sender=Pharmacy)
def create_custom_user(sender, instance, create, **kwargs):
    if create:
        if instance.status is 201:
            new_user = CustomUser.objects.create(
                username=instance.username,
                password=instance.passwprd,
                first_name=instance.first_name,
                last_name=instance.last_name,
                email=instance.email
            )

            group, created = Group.objects.get_or_create(name='Pharmacy')
            group.user_set.add(new_user)