from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import FileExtensionValidator, MaxValueValidator
from users import managers, choices
from utils.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin):
    # full_name = models.CharField(max_length=256)
    id_card = models.CharField(max_length=9, unique=True)
    # phone_number = models.CharField(max_length=13, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "id_card"


    objects = managers.UserManager()

    def __str__(self):
        return self.id_card

class UserExtraData(BaseModel):
    user = models.OneToOneField(
        "User",
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_data'
    )

    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    father_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=13, unique=True)
    profile_image = models.ImageField(
        upload_to='userExtradata/',
        null=True, blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpg', 'jpeg', 'webp', 'avif'],
                message="Faqat rasm yuklashingiz mumkin (png, jpg, jpeg, webp, avif) formatlarida"
            )
        ]
    )
    under_age_children_number = models.SmallIntegerField(
        default = 0,
        validators = [MaxValueValidator(6,message="Faqat 18 yoshga yetmagan bolalaringiz soni kerak !")]
    )
    adress = models.TextField()
    born_in = models.DateField()
    employment_at = models.DateField()
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.DecimalField(
        max_digits=16, decimal_places=2
    )
    score = models.SmallIntegerField(default=0)
    allocated_funds = models.PositiveIntegerField(default=0) # qancha pul ajratildi ushbu user uchun organization dan

    def __str__(self) -> str:
        return f"{self.name}|{self.last_name}"
    
    class Meta:
        verbose_name = "Ishchi qo'shimcha ma'lumoti"
        verbose_name_plural = "Ishchilarning qo'shimcha ma'lumotlari"
    

class UnderAgeChildren(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='under_age_children/')
    child_full_name = models.CharField(max_length=128)

    def __str__(self):
        return f"Voyaga yetmagan farzand hujjati - {self.id}"

    class Meta:
        verbose_name = "Voyaga yetmagan farzand hujjati"
        verbose_name_plural = "Voyaga yetmagan farzandlar hujjatlari"


class HandicappedDocsModel(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='handicapped/')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='docs/role/')
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
