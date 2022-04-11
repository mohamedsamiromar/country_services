from django.dispatch import receiver
from django.db.models import signals
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from restaurant.models import RestaurantBooking
from django.conf import settings


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
