# Generated by Django 4.0.5 on 2022-07-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opgradientsurveys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradientsurvey',
            name='survey_Type',
            field=models.CharField(choices=[('Static', 'Static'), ('Flowing', 'Flowing')], default='Static', max_length=20),
        ),
    ]
