# Generated by Django 2.0.13 on 2019-04-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0046_tracker_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='Assignee',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='auth.User'),
        ),
    ]