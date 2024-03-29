# Generated by Django 5.0.1 on 2024-02-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obformationpressure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OBFormatioPressureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgId', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obstat_Group', models.CharField(max_length=100)),
                ('obstat_Formation', models.CharField(max_length=100)),
                ('obstat_Member', models.CharField(max_length=100)),
                ('obmeasured_Depth', models.FloatField()),
                ('obpressure', models.FloatField()),
                ('obporosity', models.FloatField()),
                ('obpermeability', models.FloatField()),
                ('obtemperature', models.FloatField()),
                ('obremarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='OBFormatioTopsModel',
        ),
    ]
