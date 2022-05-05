from django.dispatch import receiver
from django.db.models import signals
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from restaurant.models import RestaurantBooking, RestaurantProfile
from django.conf import settings
from authentication.tasks import send_verification_email


@receiver(signals.post_save, sender=RestaurantProfile)
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.user.id)

# TODO this function related rating
# @receiver(signals.post_save, sender=RestaurantBooking)
# def send_restaurant_rating_email(sender, instance, created, **kwargs):
#     """
#             This function got called once the restaurant booking status is closed
#     """
#     if instance.status == 410:
#         template = render_to_string('../rating/template/../templates/restaurant_rating_email.html', {'info': instance})
#         email = EmailMessage(
#             'Add Your Review',
#             template,
#             settings.EMAIL_HOST_USER,
#             [instance.alien.email])
#         email.send()
