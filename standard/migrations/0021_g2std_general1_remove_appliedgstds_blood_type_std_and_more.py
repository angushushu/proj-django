# Generated by Django 4.0.2 on 2022-07-27 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0020_appliedgstds_heal_type_std_alter_gstd_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='G2Std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('HEALTYPE', 'Healtype'), ('BLOODTYPE', 'Bloodtype')], default='HEALTYPE', max_length=32)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='General1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
                ('g2std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general1', to='standard.g2std')),
            ],
            options={
                'ordering': ('value',),
            },
        ),
        migrations.RemoveField(
            model_name='appliedgstds',
            name='blood_type_std',
        ),
        migrations.RemoveField(
            model_name='appliedgstds',
            name='heal_type_std',
        ),
        migrations.CreateModel(
            name='General2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
                ('general1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general2', to='standard.general1')),
            ],
            options={
                'ordering': ('value',),
            },
        ),
        migrations.CreateModel(
            name='AppliedG2Stds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type_std', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applied_blood_type_std', to='standard.g2std')),
                ('heal_type_std', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applied_heal_type_std', to='standard.g2std')),
            ],
        ),
    ]
