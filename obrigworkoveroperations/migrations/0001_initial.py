# Generated by Django 5.0.1 on 2024-02-19 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('obrigworkover', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OBRigworkoverOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgid', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obunitname', models.CharField(max_length=50)),
                ('obop_Date', models.DateField()),
                ('obtime_from', models.TimeField()),
                ('obtime_to', models.TimeField()),
                ('obop_code', models.CharField(choices=[('None', 'None'), ('Operating', 'Operating'), ('Standby', 'Standby'), ('Mobilization', 'Mobilization'), ('Demobilization', 'Demobilization'), ('WaitingonEquipment', 'WaitingonEquipment'), ('NonProductive', 'NonProductive')], default='Operating', max_length=50)),
                ('obop_details', models.CharField(max_length=150)),
                ('obrigworkover', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obrigworkover.obrigworkover')),
            ],
        ),
    ]
