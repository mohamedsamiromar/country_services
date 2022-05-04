from django.contrib.auth.models import Group
from authentication.tasks import send_verification_email
from accounts.models import CustomUser
from django.core.mail import EmailMessage
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from autoui.settings import base
from .models import Pharmacy


@receiver(signals.post_save, sender=Pharmacy)
def get_longitude_and_latitude_for_pharmacy(sender, instance, create, **kwargs):
    if create:
        template = render_to_string('select_location_pharmacy.html', {'info': instance})
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
        new_user = CustomUser.objects.create(
            username=instance.username,
            password=12313,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email
        )
        new_user.save()
        my_group = Group.objects.create(name='Pharmacy')
        my_group.user_set.add(new_user)
        my_group.save()


@receiver(signals.post_save, sender=Pharmacy)
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.user.id)