from django.dispatch import receiver
from django.db.models import signals
from accounts.models import CustomUser
from .models import ParkingProfile
from django.contrib.auth.models import Group
from authentication.tasks import send_verification_email


@receiver(signals.post_save, sender=ParkingProfile)
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.user.id)
