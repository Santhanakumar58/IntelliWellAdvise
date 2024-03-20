# Generated by Django 5.0.1 on 2024-03-20 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TubingGradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tubingGrade', models.CharField(max_length=20)),
                ('collapsePressure', models.DecimalField(decimal_places=3, max_digits=10)),
                ('burstPressure', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TubingSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tubingSize', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TubingWeightModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tubingWeight', models.CharField(max_length=20)),
                ('tubingID', models.DecimalField(decimal_places=3, max_digits=10)),
                ('tubingSize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tubings.tubingsizemodel')),
            ],
        ),
        migrations.CreateModel(
            name='TubingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('tubingType', models.CharField(blank=True, choices=[('Tubing', 'Tubing'), ('PupJoint', 'PupJoint'), ('FlowCoupling', 'FlowCoupling'), ('SSD', 'SSD'), ('WEG', 'WEG'), ('SCSSSV', 'SCSSSV'), ('TCPGuns', 'TCPGuns'), ('Packer', 'Packer'), ('LandingNipple', 'LandingNipple'), ('BlastJoint', 'BlastJoint'), ('PerforatedPupJoint', 'PerforatedPupJoint'), ('Tubing_end', 'Tubing_end'), ('PlugbackDepth', 'PlugbackDepth'), ('Hold_up_Depth', 'Hold_up_Depth')], default='Surface', max_length=20, null=True)),
                ('tubingID', models.FloatField(blank=True, null=True)),
                ('collapsePressure', models.FloatField(blank=True, null=True)),
                ('burstPressure', models.FloatField(blank=True, null=True)),
                ('threadType', models.CharField(blank=True, choices=[('1', 'STC'), ('2', 'LTC'), ('3', 'BTC'), ('4', 'LP'), ('5', 'EUE'), ('6', 'NUE'), ('7', 'IJ'), ('8', 'VAM'), ('9', 'NEWVAM')], default='1', max_length=20, null=True)),
                ('material', models.CharField(blank=True, choices=[('1', 'Carbon_Steel'), ('2', 'CRA_9Cr'), ('3', 'CRA_13Cr'), ('4', 'Inconel')], default='1', max_length=20, null=True)),
                ('depth_From', models.FloatField(blank=True, null=True)),
                ('depth_To', models.FloatField(blank=True, null=True)),
                ('tvd_From', models.FloatField(blank=True, null=True)),
                ('tvd_To', models.FloatField(blank=True, null=True)),
                ('angle', models.FloatField(blank=True, null=True)),
                ('tubingGrade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tubingGrades', to='tubings.tubinggrademodel')),
                ('tubingSize', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tubingSizes', to='tubings.tubingsizemodel')),
                ('tubingWeight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tubingWeights', to='tubings.tubingweightmodel')),
            ],
        ),
        migrations.AddField(
            model_name='tubinggrademodel',
            name='tubingWeight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tubings.tubingweightmodel'),
        ),
    ]
