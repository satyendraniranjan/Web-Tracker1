# Generated by Django 2.0.13 on 2019-03-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0025_auto_20190301_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='OAC_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='OAR_Date',
            field=models.DateTimeField(null=True),
        ),
    ]
