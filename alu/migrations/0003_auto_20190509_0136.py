# Generated by Django 2.0.13 on 2019-05-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alu', '0002_auto_20190502_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='alupostcomtracker',
            name='Post_Reserve',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AddField(
            model_name='alupostcomtracker',
            name='Pre_Reserve',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
    ]
