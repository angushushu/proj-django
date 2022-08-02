# Generated by Django 4.0.2 on 2022-07-22 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSymp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diag', models.CharField(blank=True, default='', max_length=20)),
                ('disease_code', models.CharField(blank=True, default='', max_length=20)),
                ('admit_condition', models.CharField(blank=True, default='', max_length=20)),
                ('traditional_release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_symp', to='settlement.traditionalrelease')),
            ],
        ),
        migrations.DeleteModel(
            name='OtherSymp',
        ),
    ]
