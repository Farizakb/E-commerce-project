
from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from celery import shared_task

@shared_task
def send_mail_to_subscribers():
    email_list = ['farizakbarzada@gmail.com']

    message = 'Salam dostum'
    subject = 'Size salam getirmisik :)'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'plain'
    mail.send()
    
