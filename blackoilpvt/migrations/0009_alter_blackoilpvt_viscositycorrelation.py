# Generated by Django 4.0.5 on 2022-06-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackoilpvt', '0008_alter_blackoilpvt_pbcorrelation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackoilpvt',
            name='viscosityCorrelation',
            field=models.CharField(choices=[('Beal', 'Beal'), ('BeggsRobinson', 'BeggsRobinson'), ('Glaso', 'Glaso')], default='1', max_length=20),
        ),
    ]