from utils import choices
from django.db import models
from utils.models import BaseModel
# from employee.models import Employee
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MinLengthValidator

# class IdCards(models.Model):
#     card_id = models.CharField(max_length=9, unique=True)
#     is_active = models.BooleanField(default=False)

#     def __str__(self):
#         return self.card_id

#     class Meta:
#         verbose_name = "ID karta"
#         verbose_name_plural = "ID kartalar"


# class ApplicationStatusModel(models.Model):
#     status = models.CharField(
#         max_length=2,
#         choices=choices.ApplicationStatusChoice.choices,
#         default=choices.ApplicationStatusChoice.send
#     )
#     who_rejected = models.ForeignKey(
#         Employee,
#         on_delete=models.SET_NULL,
#         null=True
#     )
#     who_are_viewed = models.ManyToManyField(
#         Employee,
#         related_name='application_viwed_staffs'
#     )

#     def __str__(self):
#         return self.get_status_display()

#     class Meta:
#         verbose_name = "Ariza holati"
#         verbose_name_plural = "Ariza holatlari"


class Organization(BaseModel):
    name = models.CharField(
        max_length=256,
        unique=True,
        validators=[
            MinLengthValidator(5, message="Tashkilot nomini to'liqroq yozing")
        ]
    )
    tel_number = models.CharField(
        max_length=13,
        unique=True,
    )
    main_image = models.ImageField(
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
            MinLengthValidator(150, "Ilitmos tashkilot haqida ko'proq ma'lumot bering!")
        ],
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlar"


# class Event(BaseModel):
#     author = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         null=True
#     )
#     name = models.CharField(
#         max_length=100,
#         unique=True
#     )
#     spend_money = models.PositiveSmallIntegerField(
#         default=0
#     )
#     description = models.TextField(
#         validators=[
#             MinLengthValidator(100, message="Ilitmos ko'proq ma'lumot kiriting")
#         ]
#     )
#     image = models.ImageField(
#         upload_to='event/',
#         validators=[
#             FileExtensionValidator(
#                 allowed_extensions=['png', 'jpg', 'jpeg', 'webp', 'avif']
#             )
#         ]
#     )

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Tadbir"
#         verbose_name_plural = "Tadbirlar"


# class Application(BaseModel):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     author_application = models.ForeignKey(
#         Employee,
#         on_delete=models.SET_NULL,
#         null=True
#     )
#     status_application = models.ForeignKey(
#         ApplicationStatusModel,
#         on_delete=models.SET_NULL,
#         null=True
#     )

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Ariza"
#         verbose_name_plural = "Arizalar"


# class SpiritualRest(BaseModel):
#     name = models.CharField(max_length=512)
#     who_are_invited = models.ManyToManyField(
#         Employee,
#         related_name='spirtual_rest_person'
#     )
#     more_info = models.TextField(
#         validators=[
#             MinLengthValidator(
#                 100,
#                 message="Iltimos ko'proq ma'lumot kiriting !"
#             )
#         ]
#     )
#     image = models.ImageField(
#         upload_to='spirtual_rest/',
#         validators=[
#             FileExtensionValidator(
#                 allowed_extensions=['png', 'jpg', 'jpeg', 'webp'],
#                 message="Iltimos faqat rasm yuklang"
#             )
#         ]
#     )
#     additional_doc = models.FileField(
#         upload_to='additional_docs/',
#         validators=[
#             FileExtensionValidator(
#                 allowed_extensions=['pdf', 'dosx', 'txt', 'xls'],
#                 message="Fayl formati to'g'riga o'xshamaydi"
#             )
#         ],
#         null=True,
#         blank=True
#     )

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Ma'naviy dam olish"
#         verbose_name_plural = "Ma'naviy dam olishlar"


# class Accidents(BaseModel):
#     who = models.ForeignKey(
#         Employee,
#         on_delete=models.SET_NULL,
#         null=True
#     )
#     spend_money = models.PositiveBigIntegerField(default=0)
#     more_info = models.TextField()
#     prove = models.FileField(
#         upload_to='prove/',
#         validators=[
#             FileExtensionValidator(
#                 allowed_extensions=['pdf', 'docx', 'txt', 'xls'],
#                 message="Fayl formati to'g'riga o'xshamaydi"
#             )
#         ]
#     )

#     def __str__(self):
#         return f"{self.who} - {self.spend_money}"

#     class Meta:
#         verbose_name = "Baxtsiz hodisa"
#         verbose_name_plural = "Baxtsiz hodisalar"
