# Generated by Django 2.0.13 on 2019-05-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alu', '0004_auto_20190513_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alupostcomtracker',
            name='Pre_Reserve',
            field=models.CharField(blank=True, choices=[('Reserved', 'Reserved'), ('CP-INH', 'CP-INH'), ('Not Reserved', 'Not Reserved'), ('Grow', 'Grow'), ('Equipped', 'Equipped')], max_length=255),
        ),
    ]
