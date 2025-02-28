from django.db.models.signals import post_save
from django.dispatch import receiver

from authy.models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance: User, created: bool, **kwargs: dict):
    if created:
        Profile.objects.create(user=instance)
