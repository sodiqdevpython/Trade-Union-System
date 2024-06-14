# Generated by Django 5.0.6 on 2024-06-14 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0009_alter_application_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accidents',
            options={'verbose_name': 'Baxtsiz hodisa', 'verbose_name_plural': 'Baxtsiz hodisalar'},
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Ariza', 'verbose_name_plural': 'Arizalar'},
        ),
        migrations.AlterModelOptions(
            name='applicationstatusmodel',
            options={'verbose_name': 'Ariza holati', 'verbose_name_plural': 'Ariza holatlari'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Tadbir', 'verbose_name_plural': 'Tadbirlar'},
        ),
        migrations.AlterModelOptions(
            name='idcards',
            options={'verbose_name': 'ID karta', 'verbose_name_plural': 'ID kartalar'},
        ),
        migrations.AlterModelOptions(
            name='spiritualrest',
            options={'verbose_name': "Ma'naviy dam olish", 'verbose_name_plural': "Ma'naviy dam olishlar"},
        ),
    ]