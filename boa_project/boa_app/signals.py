from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response
from .tasks import send_notification_new_resp


@receiver(post_save, sender=Response)
def response_created(instance, created, **kwargs):
    if not created:
        return
    send_notification_new_resp.apply_async(
            (instance.pk, instance.content, instance.announce.author.email), countdown=10,)
