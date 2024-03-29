# Generated by Django 5.0.1 on 2024-02-15 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OBReservoirPressure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgId', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obsurvey_Date', models.DateField()),
                ('obsurvey_Type', models.CharField(choices=[('NONE', 'None'), ('RFT', 'Rft'), ('DST', 'Dst'), ('PBU', 'Pbu'), ('SHUTIN', 'Shutin')], default='1', max_length=20)),
                ('obgauge_Depth', models.DecimalField(decimal_places=3, max_digits=10)),
                ('obgauge_Pressure', models.DecimalField(decimal_places=3, max_digits=10)),
                ('obdatum_Depth', models.DecimalField(decimal_places=3, max_digits=10)),
                ('obdatum_Pressure', models.DecimalField(decimal_places=3, max_digits=10)),
                ('oblayer_permeability', models.DecimalField(decimal_places=3, max_digits=10)),
                ('oblayer_Thickness', models.DecimalField(decimal_places=3, max_digits=10)),
                ('oblayer_Skin', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
