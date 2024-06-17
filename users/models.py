from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from users import managers, choices
from utils.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=256)
    id_card = models.CharField(max_length=9, unique=True)
    phone_number = PhoneNumberField(region="UZ", unique=True)

    organization = models.ForeignKey(
        "organization.Organization", on_delete=models.CASCADE, null=True, related_name="organization")
    under_age = models.ForeignKey(
        "UnderAgeChildren", on_delete=models.CASCADE, related_name="childern", null=True, blank=True)
    handi_capped = models.ForeignKey(
        "HandicappedDocsModel", on_delete=models.CASCADE, related_name="handi", null=True, blank=True)
    role = models.ForeignKey(
        "RoleNoteModel", on_delete=models.CASCADE, related_name="role", null=True, blank=True)
    job = models.ForeignKey(
        "Job", on_delete=models.CASCADE, related_name="jobs", null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "id_card"

    REQUIRED_FIELDS = ["full_name", "phone_number"]

    objects = managers.UserManager()

    def __str__(self):
        return self.full_name


class UnderAgeChildren(BaseModel):
    file = models.FileField(
        upload_to='under_age_children/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Voyaga yetmagan farzand hujjati - {self.id}"

    class Meta:
        verbose_name = "Voyaga yetmagan farzand hujjati"
        verbose_name_plural = "Voyaga yetmagan farzandlar hujjatlari"


class HandicappedDocsModel(BaseModel):
    file = models.FileField(
        upload_to='handicapped/',
        null=True,
        blank=True
    )
    type = models.CharField(
        max_length=1,
        choices=choices.HandicappedType.choices,
        default=choices.HandicappedType.is_valid
    )

    def __str__(self):
        return f"Nogironlik hujjati - {self.id}"

    class Meta:
        verbose_name = "Nogironlik haqidagi hujjat"
        verbose_name_plural = "Nogironlik haqidagi hujjatlar"


class RoleNoteModel(BaseModel):
    file = models.FileField(
        upload_to='docs/role/',
        null=True,
        blank=True
    )
    type = models.CharField(
        max_length=1,
        choices=choices.RoleNote.choices,
        default=choices.RoleNote.is_inactive
    )

    def __str__(self):
        return f"Daftar - {self.id}"

    class Meta:
        verbose_name = "Daftar"
        verbose_name_plural = "Daftarlar"


class Job(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Ish turi"
        verbose_name_plural = "Ish turlari"
