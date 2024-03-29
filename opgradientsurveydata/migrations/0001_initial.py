# Generated by Django 4.0.5 on 2022-07-28 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opgradientsurveys', '0002_alter_gradientsurvey_survey_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradientSurveyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wellid', models.PositiveIntegerField()),
                ('gauge_Depth', models.FloatField()),
                ('gauge_Pressure', models.FloatField()),
                ('gauge_Temperature', models.FloatField()),
                ('gradientsurvey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opgradientsurveys.gradientsurvey')),
            ],
        ),
    ]
