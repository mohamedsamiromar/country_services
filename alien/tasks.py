from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


#ToDo
# user @periodic_task in schedule a task to run at a specific time every so often
@shared_task()
def send_mails():
    send_mail(
        'Django Celery',
        'send email useing django celery .',
        'samir155mohamed@gmail.com',
        ['mohamedsamiromar97@gmail.com'],
        fail_silently=False,
    )
    return send_mail()
