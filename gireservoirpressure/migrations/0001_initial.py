# Generated by Django 5.0.1 on 2024-02-15 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GIReservoirPressure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifgId', models.PositiveIntegerField()),
                ('giwellid', models.PositiveIntegerField()),
                ('gisurvey_Date', models.DateField()),
                ('gisurvey_Type', models.CharField(choices=[('NONE', 'None'), ('RFT', 'Rft'), ('DST', 'Dst'), ('PBU', 'Pbu'), ('SHUTIN', 'Shutin')], default='1', max_length=20)),
                ('gigauge_Depth', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gigauge_Pressure', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gidatum_Depth', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gidatum_Pressure', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gilayer_permeability', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gilayer_Thickness', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gilayer_Skin', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
