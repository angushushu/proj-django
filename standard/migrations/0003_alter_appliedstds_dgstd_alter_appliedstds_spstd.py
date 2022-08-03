# Generated by Django 4.0.2 on 2022-07-06 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0002_alter_appliedstds_dgstd_alter_appliedstds_spstd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedstds',
            name='dgstd',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='applied_stds', to='standard.diagstd'),
        ),
        migrations.AlterField(
            model_name='appliedstds',
            name='spstd',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='applied_stds', to='standard.specialtystd'),
        ),
    ]