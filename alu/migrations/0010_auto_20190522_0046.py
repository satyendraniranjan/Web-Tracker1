# Generated by Django 2.0.13 on 2019-05-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alu', '0009_auto_20190515_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alupostcomtracker',
            name='Final_Comments',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]
