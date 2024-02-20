# Generated by Django 4.2.1 on 2023-05-26 00:51

import constantratedrawdowntestanalysis.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConstantRateDrawdowntestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('survey_Date', models.DateField()),
                ('gauge_Depth', models.FloatField()),
                ('layer_Porosity', models.FloatField()),
                ('layer_Thickness', models.FloatField()),
                ('wellbore_Radius', models.FloatField()),
                ('total_Compressibility', models.FloatField()),
                ('initial_Res_Pres', models.FloatField()),
                ('oil_Viscosity', models.FloatField()),
                ('oil_FVF', models.FloatField()),
                ('file_Name', models.FileField(blank=True, null=True, upload_to=constantratedrawdowntestanalysis.models.filepath)),
                ('liquid_Rate', models.FloatField()),
                ('guess_Value', models.PositiveBigIntegerField(default=10)),
                ('fbhp', models.FloatField(blank=True, default=1000, null=True)),
            ],
        ),
    ]
