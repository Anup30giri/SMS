# Generated by Django 3.1.7 on 2021-04-18 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20210419_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='registrationNumber',
        ),
    ]