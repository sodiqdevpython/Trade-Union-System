from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=256)
    id_card = models.CharField(max_length=9, unique=True)
    phone_number = PhoneNumberField(region="UZ", unique=True)
    organization = models.ForeignKey("organization.Organization", on_delete=models.CASCADE, null=True, related_name="organization")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "id_card"

    REQUIRED_FIELDS = ["full_name", "phone_number"]

    objects = UserManager()

    def __str__(self):
        return self.full_name
