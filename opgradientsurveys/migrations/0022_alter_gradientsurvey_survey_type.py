# Generated by Django 4.0.5 on 2022-10-14 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opgradientsurveys', '0021_alter_gradientsurvey_survey_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradientsurvey',
            name='survey_Type',
            field=models.CharField(choices=[('Static', 'Static'), ('Flowing', 'Flowing')], default='Static', max_length=50),
        ),
    ]
