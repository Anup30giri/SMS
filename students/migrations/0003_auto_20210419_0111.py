# Generated by Django 3.1.7 on 2021-04-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
