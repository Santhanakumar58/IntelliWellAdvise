# Generated by Django 5.0.1 on 2024-02-16 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blackoilpvt', '0019_alter_blackoilpvt_gasgravity_and_more'),
        ('sublayers', '0003_alter_sublayer_area_alter_sublayer_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPDarcyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('analysis_Date', models.DateField()),
                ('layer_Permeability', models.FloatField()),
                ('layer_Thickness', models.FloatField()),
                ('drainage_Radius', models.FloatField()),
                ('wellbore_Radius', models.FloatField()),
                ('layer_Skin', models.FloatField()),
                ('current_Reservoir_Pressure', models.FloatField()),
                ('layer_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sublayers.sublayer')),
                ('pvt_Well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blackoilpvt.blackoilpvt')),
            ],
        ),
        migrations.CreateModel(
            name='GPMultirateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('analysis_Date', models.DateField()),
                ('test_Rate1', models.FloatField()),
                ('test_Pressure1', models.FloatField()),
                ('test_Rate2', models.FloatField()),
                ('test_Pressure2', models.FloatField()),
                ('test_Rate3', models.FloatField()),
                ('test_Pressure3', models.FloatField()),
                ('current_Reservoir_Pressure', models.FloatField()),
                ('layer_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sublayers.sublayer')),
                ('pvt_Well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blackoilpvt.blackoilpvt')),
            ],
        ),
        migrations.CreateModel(
            name='GPProductivityIndexModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('analysis_Date', models.DateField()),
                ('productivity_index', models.FloatField()),
                ('reservoir_Pressure', models.FloatField()),
                ('layer_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sublayers.sublayer')),
                ('pvt_Well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blackoilpvt.blackoilpvt')),
            ],
        ),
        migrations.CreateModel(
            name='GPStandingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('analysis_Date', models.DateField()),
                ('current_Test_Rate', models.FloatField()),
                ('current_Test_Pressure', models.FloatField()),
                ('current_Reservoir_Pressure', models.FloatField()),
                ('future_Reservoir_Pressure', models.FloatField()),
                ('current_Relative_Permeability', models.FloatField()),
                ('future_Relative_Permeability', models.FloatField()),
                ('layer_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sublayers.sublayer')),
                ('pvt_Well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blackoilpvt.blackoilpvt')),
            ],
        ),
        migrations.CreateModel(
            name='GPVogelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('analysis_Date', models.DateField()),
                ('vogel_Test_Rate', models.FloatField()),
                ('vogel_Test_Pressure', models.FloatField()),
                ('reservoir_Pressure', models.FloatField()),
                ('layer_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sublayers.sublayer')),
                ('pvt_Well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blackoilpvt.blackoilpvt')),
            ],
        ),
        migrations.CreateModel(
            name='GPWigginsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('analysis_Date', models.DateField()),
                ('wiggins_Test_Rate', models.FloatField()),
                ('wiggins_Test_Pressure', models.FloatField()),
                ('current_Reservoir_Pressure', models.FloatField()),
                ('future_Reservoir_Pressure', models.FloatField()),
                ('water_Cut', models.FloatField()),
                ('layer_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sublayers.sublayer')),
                ('pvt_Well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blackoilpvt.blackoilpvt')),
            ],
        ),
    ]
