# Generated by Django 5.0.1 on 2024-02-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OBGradientSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgId', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obsurvey_Date', models.DateField()),
                ('obsurvey_Type', models.CharField(choices=[('Floobng', 'Floobng'), ('Static', 'Static')], default='Static', max_length=50)),
                ('obshutin_Period', models.FloatField()),
                ('obtubinghead_Pressure', models.FloatField()),
                ('obtubinghead_Temperature', models.FloatField()),
                ('obliquid_Rate', models.FloatField()),
                ('obwater_Cut', models.FloatField()),
                ('obgas_Oil_Ratio', models.FloatField()),
            ],
        ),
    ]
