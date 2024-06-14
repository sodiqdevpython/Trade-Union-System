from django.db import models

class GenderChoices(models.TextChoices):
    Male = "E", "Erkak"
    Female = "A", "Ayol"

class HandicappedType(models.TextChoices):
    is_valid = "S", "Sog'lom"
    second = "I", "Ikkinchi gurux nogironi"
    third = "U", "Uchinchi gurux nogironi"

class RoleNote(models.TextChoices):
    is_inactive = "Y", "Yo'q"
    women_note = "A", "Ayollar daftari"
    iron_note = "T", "Temir daftar"

class ApplicationStatusChoice(models.TextChoices):
    send = "Y", "Yuborilgan"
    read = "R", "O'qilgan"
    rejected = "RJ", "Rad etilgan"