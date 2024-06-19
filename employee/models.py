from utils import choices
from django.db import models
from utils.models import BaseModel
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class UnderAgeChildren(BaseModel):
    file = models.FileField(
        upload_to='docs/under_age_children/', 
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
        upload_to='docs/handicapped/',
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

class Employee(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='employee_user')
    oranization = models.ForeignKey("organization.Organization", on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='default.png')
    gender = models.CharField(
        max_length=1, 
        choices=choices.GenderChoices.choices, 
        default=choices.GenderChoices.Male
    )
    tel_number = models.CharField(
        max_length=18,
        unique=True
    )
    id_card = models.CharField(max_length=9, unique=True)
    born_in = models.DateField()
    employment_at = models.DateField()
    under_age_children_docs = models.ForeignKey(
        UnderAgeChildren,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    under_age_children_number = models.SmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(6, message="Iltimos to'g'ri kiriting !")
        ]
    )
    handicapped = models.OneToOneField(
        HandicappedDocsModel,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='handicapped_person'
    )
    role = models.OneToOneField(
        RoleNoteModel,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='role_note',
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    allocated_funds = models.PositiveBigIntegerField(default=0) # qancha pul ajratildi ushbu user uchun organization dan
    is_verified = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.user.first_name} / {self.user.last_name}"

    class Meta:
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar"
