# Generated by Django 2.0.13 on 2019-04-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0051_auto_20190412_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsatracker',
            name='RET',
            field=models.CharField(blank=True, choices=[('Defined in LSM', 'Defined in LSM'), ('Defined in BSM', 'Defined in BSM'), ('NA', 'NA')], max_length=255),
        ),
    ]
