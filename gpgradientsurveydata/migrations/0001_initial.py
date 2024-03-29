# Generated by Django 5.0.1 on 2024-02-16 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gpgradientsurveys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPGradientSurveyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpwellid', models.PositiveIntegerField()),
                ('gpgauge_Depth', models.FloatField()),
                ('gpgauge_Pressure', models.FloatField()),
                ('gpgauge_Temperature', models.FloatField()),
                ('gpgradientsurvey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpgradientsurveys.gpgradientsurvey')),
            ],
        ),
    ]
