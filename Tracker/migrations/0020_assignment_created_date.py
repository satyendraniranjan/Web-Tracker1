# Generated by Django 2.0.13 on 2019-02-21 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0019_auto_20190221_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
