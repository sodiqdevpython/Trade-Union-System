from django.dispatch import receiver
from django.db.models.signals import post_save
from organization.models import IdCards
from django.contrib.auth.models import User

@receiver(post_save, sender=IdCards)
def create_user(sender, instance, created, *args, **kwargs):
    if created:
        User.objects.create_user(
            username=instance.card_id,
            password=instance.card_id
        )
