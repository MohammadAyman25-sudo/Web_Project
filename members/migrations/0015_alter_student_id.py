# Generated by Django 4.0.3 on 2022-07-03 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]