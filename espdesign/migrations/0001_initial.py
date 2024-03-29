# Generated by Django 4.2.1 on 2023-06-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ESPDesignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgId', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('design_Date', models.DateField()),
                ('design_Liquid', models.FloatField()),
                ('water_Cut', models.FloatField()),
                ('th_Pres', models.FloatField()),
                ('th_Temp', models.FloatField()),
                ('curr_Res_Pres', models.FloatField()),
                ('min_Pwf', models.FloatField()),
                ('gas_Oil_Ratio', models.FloatField()),
                ('gas_Separator', models.BooleanField(default=True)),
                ('gas_Separator_Efficiency', models.FloatField()),
                ('pump', models.CharField(max_length=100)),
                ('motor', models.CharField(max_length=100)),
            ],
        ),
    ]
