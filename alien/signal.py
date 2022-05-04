from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from accounts.models import CustomUser
from autoui.settings import base
from .models import Alien


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
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        new_user = CustomUser(
            username=instance.username,
            password=instance.password,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            is_active=True
        )
        new_user.save()
        my_group = Group.objects.create(name='Alien')
        my_group.user_set.add(new_user)
        my_group.save()
