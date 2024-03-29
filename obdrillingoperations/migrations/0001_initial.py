# Generated by Django 5.0.1 on 2024-02-10 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('obdrillingsummary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OBDrillingOps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgId', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obops_Date', models.DateField()),
                ('obtime_From', models.TimeField()),
                ('obtime_To', models.TimeField()),
                ('obtotalhrs', models.FloatField()),
                ('obops_Code', models.CharField(choices=[('BOPTest', 'BOPTest'), ('CasingRun', 'CasingRun'), ('Cementing', 'Cementing'), ('CementSqueeze', 'CementSqueeze'), ('Circulation', 'Circulation'), ('CoilTubing', 'CoilTubing'), ('Conditioning', 'Conditioning'), ('Coring', 'Coring'), ('DeviationSurvey', 'DeviationSurvey'), ('Drilling', 'Drilling'), ('DrillStemTest', 'DrillStemTest'), ('Fishing', 'Fishing'), ('NonProductive', 'NonProductive'), ('OperatingStatus', 'OperatingStatus'), ('Others', 'Others'), ('Perforating', 'Perforating'), ('PlugBack', 'PlugBack'), ('Reaming', 'Reaming'), ('RigDownBOP', 'RigDownBOP'), ('RigMove', 'RigMove'), ('Rigup', 'Rigup'), ('RigMaintenance', 'RigMaintenance'), ('RigRepair', 'RigRepair'), ('RigUpBOP', 'RigUpBOP'), ('ReplaceDrillingLine', 'ReplaceDrillingLine'), ('TearDown', 'TearDown'), ('TripIn', 'TripIn'), ('TripOut', 'TripOut'), ('WaitOnCement', 'WaitOnCement'), ('WaitOnWeather', 'WaitOnWeather'), ('WirelineLogs', 'WirelineLogs'), ('RunRiserEquipment', 'RunRiserEquipment'), ('RetrieveRiserEquipment', 'RetrieveRiserEquipment'), ('Safety', 'Safety'), ('SubSeaInstallation', 'SubSeaInstallation'), ('SurfaceTesting', 'SurfaceTesting'), ('Swabbing', 'Swabbing'), ('Testing', 'Testing'), ('Treating', 'Treating'), ('TubingTrip', 'TubingTrip'), ('WellCompletion', 'WellCompletion'), ('WellControl', 'WellControl')], default='Drilling', max_length=50)),
                ('obops_Summary', models.TextField(max_length=2000)),
                ('obdrillingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obdrillingsummary.obdrillingsummary')),
            ],
        ),
    ]
