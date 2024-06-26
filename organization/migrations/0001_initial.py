# Generated by Django 5.0.6 on 2024-06-16 05:58

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IdCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=9, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ID karta',
                'verbose_name_plural': 'ID kartalar',
            },
        ),
        migrations.CreateModel(
            name='Accidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('spend_money', models.PositiveBigIntegerField(default=0)),
                ('more_info', models.TextField()),
                ('prove', models.FileField(upload_to='prove/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'txt', 'xls', 'png', 'jpg', 'jpeg'], message="Fayl formati to'g'riga o'xshamaydi")])),
                ('who', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
            ],
            options={
                'verbose_name': 'Baxtsiz hodisa',
                'verbose_name_plural': 'Baxtsiz hodisalar',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status_application', models.CharField(choices=[('Y', 'Yuborilgan'), ('R', "O'qilgan"), ('RJ', 'Rad etilgan')], default='Y', max_length=2)),
                ('author_application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
            ],
            options={
                'verbose_name': 'Ariza',
                'verbose_name_plural': 'Arizalar',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('spend_money', models.PositiveSmallIntegerField(default=0)),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(100, message="Ilitmos ko'proq ma'lumot kiriting")])),
                ('image', models.ImageField(upload_to='event/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'webp', 'avif'])])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tadbir',
                'verbose_name_plural': 'Tadbirlar',
            },
        ),
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
                ('id_cards', models.ManyToManyField(related_name='employee_id_card', to='organization.idcards')),
                ('staffs', models.ManyToManyField(related_name='staffs_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tashkilot',
                'verbose_name_plural': 'Tashkilotlar',
            },
        ),
        migrations.CreateModel(
            name='SpiritualRest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('spend_money', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=512)),
                ('more_info', models.TextField(validators=[django.core.validators.MinLengthValidator(100, message="Iltimos ko'proq ma'lumot kiriting !")])),
                ('image', models.ImageField(upload_to='spirtual_rest/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'webp'], message='Iltimos faqat rasm yuklang')])),
                ('additional_doc', models.FileField(blank=True, null=True, upload_to='additional_docs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'dosx', 'txt', 'xls'], message="Fayl formati to'g'riga o'xshamaydi")])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
                ('who_are_invited', models.ManyToManyField(related_name='spirtual_rest_person', to='employee.employee')),
            ],
            options={
                'verbose_name': "Ma'naviy dam olish",
                'verbose_name_plural': "Ma'naviy dam olishlar",
            },
        ),
    ]
