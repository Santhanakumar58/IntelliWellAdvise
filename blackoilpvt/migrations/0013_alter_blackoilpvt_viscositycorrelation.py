# Generated by Django 4.0.5 on 2022-06-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackoilpvt', '0012_alter_blackoilpvt_pbcorrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackoilpvt',
            name='viscosityCorrelation',
            field=models.CharField(choices=[('_Beal', 'Beal'), ('_Glaso', 'Glaso'), ('_BeggsRobinson', 'BeggsRobinson')], default='1', max_length=20),
        ),
    ]