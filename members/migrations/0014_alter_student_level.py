# Generated by Django 4.0.3 on 2022-07-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_student_inactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(max_length=100),
        ),
    ]
