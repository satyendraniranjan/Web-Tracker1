# Generated by Django 2.0.13 on 2019-04-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0056_auto_20190416_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='Assignee',
            field=models.CharField(max_length=255),
        ),
    ]