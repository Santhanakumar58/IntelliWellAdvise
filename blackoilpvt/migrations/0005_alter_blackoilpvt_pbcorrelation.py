# Generated by Django 4.0.5 on 2022-06-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackoilpvt', '0004_rename_sampledate_blackoilpvt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackoilpvt',
            name='pbCorrelation',
            field=models.CharField(choices=[('STANDING', 'Standing'), ('Glasso', 'Glasso'), ('Marhoun', 'Marhoun'), {'VasquezBeggs', 'Vasquez_Beggs'}, ('Petrosky_Farshad', 'PetroskyFarshad')], default='1', max_length=20),
        ),
    ]
