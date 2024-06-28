from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator, MinLengthValidator

from utils.models import BaseModel
from users.models import User
from organization import choices

class IDCards(BaseModel):
    id_card = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return self.id_card
    
    class Meta:
        verbose_name = "ID karta"
        verbose_name_plural = "ID kartalar"

class Money(BaseModel):
    current_money = models.DecimalField(default=0, decimal_places=4, max_digits=10)
    
    def __str__(self):
        return str(self.current_money)

    class Meta:
        verbose_name = "Pul"
        verbose_name_plural = "Pul"

class Organization(BaseModel):
    title = models.CharField(
        max_length=256,
        unique=True,
        validators=[
            MinLengthValidator(5, message="Tashkilot nomini to'liqroq yozing")
        ]
    )
    phone_number = PhoneNumberField(region="UZ", unique=True)
    image = models.ImageField(
        upload_to='organization/images/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpg', 'jpeg', 'webp', 'avif'],
                message="Faqat rasm yuklashingiz mumkin (png, jpg, jpeg, webp, avif) formatlarida"
            )
        ]
    )

    description = models.TextField(
        validators=[
            MinLengthValidator(
                150, "Ilitmos tashkilot haqida ko'proq ma'lumot bering!")
        ],
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlar"


class Event(BaseModel):
    title = models.CharField(
        max_length=100,
        unique=True
    )
    spend_money = models.DecimalField(
        max_digits=9, decimal_places=0
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(
                100, message="Ilitmos ko'proq ma'lumot kiriting")
        ]
    )
    image = models.ImageField(
        upload_to='event/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpg', 'jpeg', 'webp', 'avif']
            )
        ]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tadbir"
        verbose_name_plural = "Tadbirlar"


class Application(BaseModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author_application = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, related_name="application"
    )
    status_application = models.CharField(
        max_length=128, choices=choices.ApplicationStatusChoice.choices, default=choices.ApplicationStatusChoice.send)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"


class SpiritualRest(BaseModel):
    title = models.CharField(max_length=512)
    description = models.TextField(
        validators=[
            MinLengthValidator(
                100,
                message="Iltimos ko'proq ma'lumot kiriting !"
            )
        ]
    )
    image = models.ImageField(
        upload_to='spirtual_rest/',
        validators=[
            FileExtensionValidator(
                  allowed_extensions=['png', 'jpg', 'jpeg', 'webp'],
                  message="Iltimos faqat rasm yuklang"
            )
        ]
    )
    user = models.ManyToManyField(
        User,
        related_name='users'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ma'naviy dam olish"
        verbose_name_plural = "Ma'naviy dam olishlar"


class Accidents(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, related_name="accidents"
    )
    spend_money = models.DecimalField(max_digits=6, decimal_places=2)
    more_info = models.TextField()
    prove = models.FileField(
        upload_to='accidents/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'docx', 'txt', 'xls'],
                message="Fayl formati to'g'riga o'xshamaydi"
            )
        ]
    )

    def __str__(self):
        return f"{self.user} - {self.spend_money}"

    class Meta:
        verbose_name = "Baxtsiz hodisa"
        verbose_name_plural = "Baxtsiz hodisalar"
