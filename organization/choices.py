from django.db.models import TextChoices


class ApplicationStatusChoice(TextChoices):
    send = "Y", "Yuborilgan"
    read = "R", "O'qilgan"
    rejected = "RJ", "Rad etilgan"
