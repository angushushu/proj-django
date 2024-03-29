# Generated by Django 4.0.2 on 2022-07-06 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0005_alter_appliedstds_dgstd_alter_appliedstds_spstd'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedDgStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_dgstd', to='standard.diagstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedSpStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_spstd', to='standard.specialtystd')),
            ],
        ),
        migrations.DeleteModel(
            name='AppliedStds',
        ),
    ]
