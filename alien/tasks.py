from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


# ToDo
# user @periodic_task in schedule a task to run at a specific time every so often
@shared_task()
def num_sun(x, y):
    return x + y
