# Generated by Django 4.0.2 on 2022-07-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0015_alter_appliedgstds_admit_condition_std_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gstd',
            name='type',
            field=models.CharField(choices=[('NATIONALITY', 'Nationality'), ('ETHNICITY', 'Ethnicity')], default='NATIONALITY', max_length=16),
        ),
    ]
