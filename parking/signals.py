from django.dispatch import receiver
from django.db.models import signals
from accounts.models import CustomUser
from .models import ParkingProfile
from django.contrib.auth.models import Group


@receiver(signals.post_save, sender=ParkingProfile)
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
        my_group = Group.objects.create(name='Parking')
        my_group.user_set.add(new_user)
        my_group.save()
