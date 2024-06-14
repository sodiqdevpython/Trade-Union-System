# Generated by Django 5.0.6 on 2024-06-14 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_handicapped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_note', to='employee.rolenotemodel'),
        ),
    ]
