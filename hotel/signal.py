from django.dispatch import receiver
from authentication.tasks import send_verification_email
from django.db.models import signals
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from restaurant.models import RestaurantProfile
from .models import Hotel


@receiver(signals.post_save, sender=Hotel)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        new_user = CustomUser(
            username=instance.username,
            password=12313,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email
        )
        new_user.save()
        my_group = Group.objects.create(name='Hotel')
        my_group.user_set.add(new_user)
        my_group.save()


@receiver(signals.post_save, sender=Hotel)
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.user.id)
