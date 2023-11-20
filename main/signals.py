from django.dispatch import receiver
from django.db.models.signals import post_save

from main.models import Like
from main.tasks import like_created


@receiver(post_save, sender=Like)
def NewLikeToMail(sender, instance, created, **kwargs):
    if created:
        like_created.delay()