# Generated by Django 4.0.5 on 2022-06-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackoilpvt', '0009_alter_blackoilpvt_viscositycorrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackoilpvt',
            name='viscosityCorrelation',
            field=models.CharField(choices=[('Beal', 'Beal'), ('Beggs_Robinson', 'BeggsRobinson'), ('Glaso', 'Glaso')], default='1', max_length=20),
        ),
    ]
