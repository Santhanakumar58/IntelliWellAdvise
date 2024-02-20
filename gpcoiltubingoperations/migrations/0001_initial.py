# Generated by Django 5.0.1 on 2024-02-18 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gpcoiltubing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPCoiltubingOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpfgid', models.PositiveIntegerField()),
                ('gpwellid', models.PositiveIntegerField()),
                ('gpctname', models.CharField(max_length=50)),
                ('gpop_Date', models.DateField()),
                ('gptime_from', models.TimeField()),
                ('gptime_to', models.TimeField()),
                ('gptotalhrs', models.FloatField()),
                ('gpop_code', models.CharField(choices=[('None', 'None'), ('Operating', 'Operating'), ('Standby', 'Standby'), ('Mobilization', 'Mobilization'), ('Demobilization', 'Demobilization'), ('WaitingonEquipment', 'WaitingonEquipment'), ('NonProductive', 'NonProductive')], default='Operating', max_length=50)),
                ('gpop_details', models.CharField(max_length=150)),
                ('gpcoiltubingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpcoiltubing.gpcoiltubing')),
            ],
        ),
    ]
