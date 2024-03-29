# Generated by Django 5.0.1 on 2024-02-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WIReservoirPressureEstimationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgid', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wianalysis_Date', models.DateField()),
                ('wilayer_Permeability', models.FloatField()),
                ('wilayer_Thickness', models.FloatField()),
                ('wilayer_Porosity', models.FloatField()),
                ('witotal_Compressibility', models.FloatField()),
                ('wimu_oil', models.FloatField()),
                ('wioil_FVF', models.FloatField()),
                ('wiwellbore_Radius', models.FloatField()),
                ('wioil_Prod_Rate', models.FloatField()),
                ('wiini_Res_Pres', models.FloatField()),
                ('widrainage_Radius', models.FloatField()),
            ],
        ),
    ]
