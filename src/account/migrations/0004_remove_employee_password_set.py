# Generated by Django 4.2.9 on 2024-02-02 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_employee_is_active_alter_employee_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='password_set',
        ),
    ]