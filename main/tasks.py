import time

from celery import shared_task
from django.core.mail import send_mail
from .models import Like


@shared_task
def like_created():
    subject = f'Order nr.'
    message = f'Dear vitaly,\n\n' f'You have successfully placed an order.' f'Your order ID is .'
    time.sleep(3)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          ['vetrof@gmail.com', ])

    return mail_sent
