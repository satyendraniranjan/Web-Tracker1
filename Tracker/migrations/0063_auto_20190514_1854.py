# Generated by Django 2.0.13 on 2019-05-14 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0062_auto_20190513_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='Activity1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='Tracker.activity'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='Activity',
            field=models.CharField(blank=True, choices=[('C&I', 'C&I'), ('Troubleshoot', 'Troubleshoot'), ('LATP Testing', 'LATP Testing'), ('FATP Testing', 'FATP Testing'), ('Pre-Integration', 'Pre-Integration'), ('Update to FE', 'Update to FE')], default='C&I', max_length=255),
            preserve_default=False,
        ),
    ]
