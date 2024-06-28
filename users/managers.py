from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, id_card, password=None, **extra_fields):
        if not id_card:
            raise ValueError("Bu yerda passport seriya raqami bo'lishi kerak")
        user = self.model(id_card=id_card, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, id_card, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("is_superuser", True)

        user = self.create_user(
                                id_card=id_card, password=password, **extra_fields)
        user.save(using=self.db)
        return user
