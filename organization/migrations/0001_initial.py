# Generated by Django 5.0.6 on 2024-06-14 11:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, unique=True, validators=[django.core.validators.MinLengthValidator(5, message="Tashkilot nomini to'liqroq yozing")])),
                ('tel_number', models.CharField(max_length=13, unique=True)),
                ('main_image', models.ImageField(upload_to='organization/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'webp', 'avif'], message='Faqat rasm yuklashingiz mumkin (png, jpg, jpeg, webp, avif) formatlarida')])),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(150, "Ilitmos tashkilot haqida ko'proq ma'lumot bering!")])),
            ],
            options={
                'verbose_name': 'Tashkilot',
                'verbose_name_plural': 'Tashkilotlar',
            },
        ),
    ]
