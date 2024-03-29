# Generated by Django 4.0.2 on 2022-07-11 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0009_alter_diag_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmitCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='AdmitConditionStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AdmitPath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='AdmitPathStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AnaesthesiaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='AnaesthesiaTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='BloodGroupStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='BloodTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ContactRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='ContactRelationStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CUType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='CUTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='EthnicityStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='GenderStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='HealType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='HealTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='HospReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='HospReasonStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='IdType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='IdTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MarriageStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='MarriageStatStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='NationalityStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='NewbornAdmitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='NewbornAdmitTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='OpLvl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='OpLvlStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='PaymentTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PurchaseMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='PurchaseMethodStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RecordQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='RecordQualityStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ReleaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='ReleaseTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Rh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='RhStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SettlementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='SettlementTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SpecialPersonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='SpecialPersonTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='WoundHealingLvl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('label', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='WoundHealingLvlStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AppliedWoundHealingLvlStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_woundhealinglvlstd', to='standard.woundhealinglvlstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedSpecialPersonTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_appliedspecialpersontypestd', to='standard.specialpersontypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedSettlementTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_settlementtypestd', to='standard.settlementtypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedRhStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_rhstd', to='standard.rhstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedReleaseTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_appliedreleasetypestd', to='standard.releasetypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedRecordQualityStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_recordqualitystd', to='standard.recordqualitystd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedPurchaseMethodStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_purchasemethodstd', to='standard.purchasemethodstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedPaymentTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_paymenttypestd', to='standard.paymenttypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedOpLvlStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_oplvlstd', to='standard.oplvlstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedNewbornAdmitTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_newbornadmittypestd', to='standard.newbornadmittypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedNationalityStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_nationalitystd', to='standard.nationalitystd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedMarriageStatStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_marriagestatstd', to='standard.marriagestatstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedIdTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_idtypestd', to='standard.idtypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedHospReasonStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_hospreasonstd', to='standard.hospreasonstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedHealTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_healtypestd', to='standard.healtypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedGenderStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_genderstd', to='standard.genderstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedEthnicityStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_ethnicitystd', to='standard.ethnicitystd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedCUTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_cutypestd', to='standard.cutypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedContactRelationStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_contactrelationstd', to='standard.contactrelationstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedBloodTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_bloodtypestd', to='standard.bloodtypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedBloodGroupStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_bloodgroupstd', to='standard.bloodgroupstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedAnaesthesiaTypeStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_anaesthesiatypestd', to='standard.anaesthesiatypestd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedAdmitPathStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_admitpathstd', to='standard.admitpathstd')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedAdmitConditionStd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_admitconditionstd', to='standard.admitconditionstd')),
            ],
        ),
    ]
