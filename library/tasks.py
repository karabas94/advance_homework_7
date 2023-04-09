from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_reminder(email, text):
    send_mail(
        'Reminder',
        text,
        'admin@admin.com',
        [email],
        fail_silently=False,
    )
