from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import User


@shared_task
def send_notification_new_resp(pk, content, announce_author_email):
    html_content = render_to_string(
        'response_added_email.html',
        {
            'text': content,
            'link': f'{settings.SITE_URL}/announce/{pk}',
        }
    )
    msg = EmailMultiAlternatives(
        subject='Вам оставили отклик',
        body=content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[announce_author_email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def send_notification_accepted_resp(resp_author_email, announce_author):
    html_content = render_to_string(
        'response_accepted_email.html',
        {
            'user': announce_author,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Отклик принят',
        body=f'Привет! Пользователь {announce_author} принял ваш отклик',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[resp_author_email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def send_news(announce_title, announce_content):
    users_emails = set(User.objects.values_list('email', flat=True))
    html_content = render_to_string(
        'news_email.html',
        {
            'title': announce_title,
            'content': announce_content,
            'link': f'{settings.SITE_URL}',
        }
    )
    # for email in users_emails:
    msg = EmailMultiAlternatives(
        subject='Новости',
        body=f'Привет! Посмотри новое объявление {announce_title} на сайте',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=users_emails,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
