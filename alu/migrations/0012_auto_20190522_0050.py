# Generated by Django 2.0.13 on 2019-05-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alu', '0011_auto_20190522_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alursatracker',
            name='Technology',
            field=models.CharField(choices=[('800 CDMA', '800 CDMA'), ('1900 CDMA', '1900 CDMA'), ('800 FDD', '800 FDD'), ('1900 FDD', '1900 FDD'), ('2.5 TDD', '2.5 TDD'), ('700 FDD', '700 FDD'), ('1900 FDD;800 FDD', '1900 FDD;800 FDD'), ('1900 CDMA;800 CDMA', '1900 CDMA;800 CDMA')], max_length=255),
        ),
    ]
