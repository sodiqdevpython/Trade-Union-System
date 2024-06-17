from django.db.models import TextChoices


class GenderChoices(TextChoices):
    Male = "E", "Erkak"
    Female = "A", "Ayol"


class HandicappedType(TextChoices):
    is_valid = "S", "Sog'lom"
    second = "I", "Ikkinchi gurux nogironi"
    third = "U", "Uchinchi gurux nogironi"


class RoleNote(TextChoices):
    is_inactive = "Y", "Yo'q"
    women_note = "A", "Ayollar daftari"
    iron_note = "T", "Temir daftar"
