# Generated by Django 4.0.4 on 2022-05-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_students_delete_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='gpa',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
