# Generated by Django 5.0.6 on 2024-06-14 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_idcards_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accidents',
            name='type',
        ),
    ]