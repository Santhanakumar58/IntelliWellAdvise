# Generated by Django 4.2.1 on 2023-07-21 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blackoilpvt', '0019_alter_blackoilpvt_gasgravity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SRPDesignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('design_Date', models.DateField()),
                ('design_Liquid', models.FloatField()),
                ('water_Cut', models.FloatField()),
                ('gas_Oil_Ratio', models.FloatField()),
                ('water_spgr', models.FloatField(default=1.0)),
                ('th_Pres', models.FloatField()),
                ('th_Temp', models.FloatField()),
                ('curr_Res_Pres', models.FloatField()),
                ('min_Pwf', models.FloatField()),
                ('pump_Depth', models.FloatField()),
                ('fluid_Level', models.FloatField()),
                ('pumping_Speed', models.PositiveIntegerField()),
                ('surface_Stroke_Length', models.FloatField()),
                ('plunger_Dia', models.FloatField()),
                ('anchored', models.BooleanField(default=True)),
                ('rod_No', models.CharField(max_length=100)),
                ('pvt_Well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blackoilpvt.blackoilpvt')),
            ],
        ),
    ]
