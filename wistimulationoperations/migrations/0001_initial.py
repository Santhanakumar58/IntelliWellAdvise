# Generated by Django 5.0.1 on 2024-02-18 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wistimulation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WIStimulationOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgid', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wiunitname', models.CharField(max_length=50)),
                ('wiop_Date', models.DateField()),
                ('witime_from', models.TimeField()),
                ('witime_to', models.TimeField()),
                ('wiop_code', models.CharField(choices=[('None', 'None'), ('Operating', 'Operating'), ('Standby', 'Standby'), ('Mobilization', 'Mobilization'), ('Demobilization', 'Demobilization'), ('WaitingonEquipment', 'WaitingonEquipment'), ('NonProductive', 'NonProductive')], default='Operating', max_length=50)),
                ('wiop_details', models.CharField(max_length=150)),
                ('wistimulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wistimulation.wistimulation')),
            ],
        ),
    ]
