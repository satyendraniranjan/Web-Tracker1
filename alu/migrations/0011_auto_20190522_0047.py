# Generated by Django 2.0.13 on 2019-05-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alu', '0010_auto_20190522_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alupostcomtracker',
            name='Final_Comments',
            field=models.TextField(blank=True, default=''),
        ),
    ]
