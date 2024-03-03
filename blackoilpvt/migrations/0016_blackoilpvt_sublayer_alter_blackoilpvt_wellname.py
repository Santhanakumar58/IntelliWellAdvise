# Generated by Django 4.0.5 on 2022-07-20 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sublayers', '0001_initial'),
        ('blackoilpvt', '0015_alter_blackoilpvt_pbcorrelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackoilpvt',
            name='subLayer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sublayers.sublayer'),
        ),
        migrations.AlterField(
            model_name='blackoilpvt',
            name='wellName',
            field=models.CharField(max_length=100),
        ),
    ]