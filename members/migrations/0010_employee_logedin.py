# Generated by Django 4.0.3 on 2022-06-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='logedin',
            field=models.BooleanField(default=False),
        ),
    ]
