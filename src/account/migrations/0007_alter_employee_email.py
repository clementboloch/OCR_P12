# Generated by Django 4.2.9 on 2024-02-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_employee_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
