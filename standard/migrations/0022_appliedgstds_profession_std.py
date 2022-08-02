# Generated by Django 4.0.2 on 2022-07-28 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0021_g2std_general1_remove_appliedgstds_blood_type_std_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedgstds',
            name='profession_std',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applied_profession_std', to='standard.gstd'),
        ),
    ]
