from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from restaurant.models import RestaurantProfile
from . models import Hotel


@receiver(signals.post_save, sender=Hotel)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        new_user = CustomUser(
            username=instance.username,
            password=123123,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            is_active=True
        )
        new_user.save()
        my_group = Group.objects.create(name='Hotel')
        my_group.user_set.add(new_user)
        my_group.save()

