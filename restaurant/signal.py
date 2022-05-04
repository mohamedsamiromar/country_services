from django.dispatch import receiver
from django.db.models import signals
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from restaurant.models import RestaurantBooking, RestaurantProfile
from django.conf import settings


@receiver(signals.post_save, sender=RestaurantProfile)
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
        my_group = Group.objects.create(name='Restaurant')
        my_group.user_set.add(new_user)
        my_group.save()


@receiver(signals.post_save, sender=RestaurantBooking)
def send_restaurant_rating_email(sender, instance, created, **kwargs):
    """
            This function got called once the restaurant booking status is closed
    """
    if instance.status == 410:
        template = render_to_string('../rating/template/../templates/restaurant_rating_email.html', {'info': instance})
        email = EmailMessage(
            'Add Your Review',
            template,
            settings.EMAIL_HOST_USER,
            [instance.alien.email])
        email.send()
