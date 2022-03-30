from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status


@shared_task
def send_mail_task():
    print("Mail sending.......")
    subject = 'welcome to Autoui world'
    message = 'Hi thank you for joying in Autoui'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['yourmail@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    return Response({"MSG": "Mail has been sent........"}, status=status.HTTP_200_OK)
