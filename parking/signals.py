from django.dispatch import receiver
from django.db.models import signals
from accounts.models import CustomUser
from .models import Parking
from django.contrib.auth.models import Group


@receiver(signals.post_save, sender=Parking)
def create_custom_user(sender, instance, create, **kwargs):
    if create:
        if instance.status is 201:
            new_user = CustomUser.objects.create(
                username=instance.username,
                first_name=instance.first_name,
                last_name=instance.last_name,
                email=instance.email
            )

            group, created = Group.objects.get_or_create(name='Parking')
            group.user_set.add(new_user)
