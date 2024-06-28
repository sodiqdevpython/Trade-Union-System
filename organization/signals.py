from django.dispatch import receiver
from django.db.models.signals import post_save
from organization.models import IDCards
from users.models import User

@receiver(post_save, sender=IDCards)
def create_verified_user(sender, instance, created, *args, **kwargs):
    if created:
        User.objects.create_user(id_card=instance.id_card, password=instance.id_card)