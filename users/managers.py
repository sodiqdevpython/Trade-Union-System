from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, full_name, id_card, phone_number, organization, password=None, **extra_fields):
        if not full_name:
            raise ValueError("Bu yerda I.F.O bo'lishi kerak")
        if not id_card:
            raise ValueError("Bu yerda passport seriya raqami bo'lishi kerak")
        if not phone_number:
            raise ValueError("Bu yerda telefon raqam bo'lishi kerak")

        user = self.model(full_name=full_name, id_card=id_card,
                          phone_number=phone_number, organization=organization, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, full_name, id_card, phone_number, password, organization=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("is_superuser", True)

        user = self.create_user(full_name=full_name,
                                id_card=id_card, phone_number=phone_number, password=password, organization=organization, **extra_fields)
        user.save(using=self.db)
        return user
