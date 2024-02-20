# Generated by Django 5.0.1 on 2024-02-19 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('girigworkover', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GIRigworkoverOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifgid', models.PositiveIntegerField()),
                ('giwellid', models.PositiveIntegerField()),
                ('giunitname', models.CharField(max_length=50)),
                ('giop_Date', models.DateField()),
                ('gitime_from', models.TimeField()),
                ('gitime_to', models.TimeField()),
                ('giop_code', models.CharField(choices=[('None', 'None'), ('Operating', 'Operating'), ('Standby', 'Standby'), ('Mobilization', 'Mobilization'), ('Demobilization', 'Demobilization'), ('WaitingonEquipment', 'WaitingonEquipment'), ('NonProductive', 'NonProductive')], default='Operating', max_length=50)),
                ('giop_details', models.CharField(max_length=150)),
                ('girigworkover', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girigworkover.girigworkover')),
            ],
        ),
    ]
