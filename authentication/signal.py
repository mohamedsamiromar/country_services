from django.db.models import signals
from authentication.tasks import send_verification_email
from django.dispatch import receiver
from accounts.models import CustomUser

@receiver(signals.post_save, sender=CustomUser)
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        send_verification_email.delay(instance.pk)
