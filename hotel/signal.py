from django.dispatch import receiver
from authentication.tasks import send_verification_email
from django.db.models import signals
from .models import Hotel


@receiver(signals.post_save, sender=Hotel)
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.user.id)
