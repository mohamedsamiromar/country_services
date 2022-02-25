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
    if created and instance:
        new_user = CustomUser(
            username=instance.username,
            email=instance.email,
            first_name=instance.first_name,
            last_name=instance.last_name,
        )
        new_user.save()
        print('created')

        group, created = Group.objects.get_or_create(name='Alien')
        group.user_set.add(new_user)
