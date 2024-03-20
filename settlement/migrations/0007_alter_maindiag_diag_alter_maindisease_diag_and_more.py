# Generated by Django 4.0.2 on 2022-08-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0006_alter_settlement_settle_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindiag',
            name='diag',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='maindisease',
            name='diag',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='mainsymp',
            name='diag',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='otherdiag',
            name='diag',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='t_emergency_diag',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='w_emergency_diag',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]