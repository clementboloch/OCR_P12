# Generated by Django 4.2.9 on 2024-02-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_employee_password_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
