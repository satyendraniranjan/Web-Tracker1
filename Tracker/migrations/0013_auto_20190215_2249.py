# Generated by Django 2.1.4 on 2019-02-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0012_auto_20190215_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='Frequency_Earfcn_Checked_from_LSM_BSM',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Required', 'Not Required')], max_length=500),
        ),
    ]
