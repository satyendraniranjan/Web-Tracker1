# Generated by Django 2.0.13 on 2019-04-03 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0043_auto_20190403_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsatracker',
            old_name='user',
            new_name='User_Name',
        ),
    ]
