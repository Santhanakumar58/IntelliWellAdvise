# Generated by Django 5.0.1 on 2024-02-09 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GICasingGradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gicasingGrade', models.CharField(max_length=20)),
                ('gicollapsePressure', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gi', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='GICasingSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gicasingSize', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GICasingWeightModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gicasingWeight', models.CharField(max_length=20)),
                ('gicasingID', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gicasingSize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gicasings.gicasingsizemodel')),
            ],
        ),
        migrations.CreateModel(
            name='GICasingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifgid', models.PositiveIntegerField()),
                ('giwellid', models.PositiveIntegerField()),
                ('gicasingType', models.CharField(blank=True, choices=[('Surface', 'Surface'), ('Conductor', 'Conductor'), ('Internediate_1', 'Internediate1'), ('Intermediate_2', 'Intermediate2'), ('Intermediate_3', 'Intermediate2'), ('Liner_casing', 'Linercasing'), ('Production_Casing', 'ProductionCasing'), ('Production_Liner', 'ProductionLiner')], default='Surface', max_length=20, null=True)),
                ('gicasingID', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('gicollapsePressure', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('giburstPressure', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('githreadType', models.CharField(blank=True, choices=[('1', 'STC'), ('2', 'LTC'), ('3', 'BTC'), ('4', 'LP'), ('5', 'EUE'), ('6', 'NUE'), ('7', 'IJ'), ('8', 'VAM'), ('9', 'NEWVAM')], default='1', max_length=20, null=True)),
                ('gimaterial', models.CharField(blank=True, choices=[('1', 'Carbon_Steel'), ('2', 'CRA_9Cr'), ('3', 'CRA_13Cr'), ('4', 'Inconel')], default='1', max_length=20, null=True)),
                ('gishoedepth', models.FloatField()),
                ('gifloatCollar', models.FloatField()),
                ('gihangerDepth', models.FloatField()),
                ('gicementTop', models.FloatField()),
                ('gicasingGrade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casingGrades', to='gicasings.gicasinggrademodel')),
                ('gicasingSize', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casingSizes', to='gicasings.gicasingsizemodel')),
                ('gicasingWeight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casingWeights', to='gicasings.gicasingweightmodel')),
            ],
        ),
        migrations.AddField(
            model_name='gicasinggrademodel',
            name='gicasingWeight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gicasings.gicasingweightmodel'),
        ),
    ]