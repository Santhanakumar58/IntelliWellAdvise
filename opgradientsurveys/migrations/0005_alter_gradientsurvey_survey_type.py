# Generated by Django 4.0.5 on 2022-08-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opgradientsurveys', '0004_alter_gradientsurvey_survey_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradientsurvey',
            name='survey_Type',
            field=models.CharField(choices=[('Flowing', 'Flowing'), ('Static', 'Static')], default='Static', max_length=20),
        ),
    ]
