# Generated by Django 4.2.1 on 2023-05-09 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('differentialliberation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DifferentialLiberationdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pressure', models.FloatField()),
                ('solution_gor', models.FloatField()),
                ('relative_oil_volume', models.FloatField()),
                ('relative_total_volume', models.FloatField()),
                ('oil_density', models.FloatField(blank=True, null=True)),
                ('deviation_factor', models.FloatField(blank=True, null=True)),
                ('gas_fvf', models.FloatField()),
                ('incremental_gas_gravity', models.FloatField()),
                ('differentialliberation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='differentialliberation.differentialliberationmodel')),
            ],
        ),
    ]