# Generated by Django 5.0.1 on 2024-02-16 11:33

import gpdrawdowntestanalysis.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPDrawdowntest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpfgid', models.PositiveIntegerField()),
                ('gpwellid', models.PositiveIntegerField()),
                ('gpsurvey_Date', models.DateField()),
                ('gpgauge_Depth', models.FloatField()),
                ('gplayer_Porosity', models.FloatField()),
                ('gplayer_Thickness', models.FloatField()),
                ('gpwellbore_Radius', models.FloatField()),
                ('gptotal_Compressibility', models.FloatField()),
                ('gpinitial_Res_Pres', models.FloatField()),
                ('gpoil_Viscosity', models.FloatField()),
                ('gpoil_FVF', models.FloatField()),
                ('gppvt_Well', models.CharField(blank=True, max_length=50, null=True)),
                ('gpfile_Name', models.FileField(blank=True, null=True, upload_to=gpdrawdowntestanalysis.models.filepath)),
                ('gptest_Type', models.CharField(blank=True, choices=[('Constant_Rate', 'Constant_Rate'), ('Constant_Pressure', 'Constant_Pressure'), ('Multi_Rate', 'Multi_Rate')], default='Constant_Rate', max_length=50, null=True)),
                ('gpliquid_Rate', models.FloatField()),
                ('gpguess_Value', models.PositiveBigIntegerField(default=10)),
                ('gpfbhp', models.FloatField(blank=True, default=1000, null=True)),
            ],
        ),
    ]
