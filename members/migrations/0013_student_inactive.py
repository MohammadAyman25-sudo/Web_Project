# Generated by Django 4.0.3 on 2022-07-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_student_female'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='inactive',
            field=models.BooleanField(default=False),
        ),
    ]
