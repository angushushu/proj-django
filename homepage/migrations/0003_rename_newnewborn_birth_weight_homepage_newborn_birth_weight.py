# Generated by Django 4.0.2 on 2022-06-28 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_remove_homepage_newborn_birth_weight_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='newnewborn_birth_weight',
            new_name='newborn_birth_weight',
        ),
    ]
