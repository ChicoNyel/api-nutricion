# Generated by Django 4.1.2 on 2022-10-17 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
