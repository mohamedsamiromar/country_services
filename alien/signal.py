from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from accounts.models import CustomUser
from autoui.settings import base
from .models import Alien
from authentication.tasks import send_verification_email


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
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        send_verification_email.delay(instance.pk)
