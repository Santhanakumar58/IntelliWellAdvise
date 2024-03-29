# Generated by Django 5.0.1 on 2024-02-09 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WICasingGradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wicasingGrade', models.CharField(max_length=20)),
                ('wicollapsePressure', models.DecimalField(decimal_places=3, max_digits=10)),
                ('wiburstPressure', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='WICasingSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wicasingSize', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WICasingWeightModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wicasingWeight', models.CharField(max_length=20)),
                ('wicasingID', models.DecimalField(decimal_places=3, max_digits=10)),
                ('wicasingSize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wicasings.wicasingsizemodel')),
            ],
        ),
        migrations.CreateModel(
            name='WICasingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgid', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wicasingType', models.CharField(blank=True, choices=[('Surface', 'Surface'), ('Conductor', 'Conductor'), ('Internediate_1', 'Internediate1'), ('Intermediate_2', 'Intermediate2'), ('Intermediate_3', 'Intermediate2'), ('Liner_casing', 'Linercasing'), ('Production_Casing', 'ProductionCasing'), ('Production_Liner', 'ProductionLiner')], default='Surface', max_length=20, null=True)),
                ('wicasingID', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('wicollapsePressure', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('wiburstPressure', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('withreadType', models.CharField(blank=True, choices=[('1', 'STC'), ('2', 'LTC'), ('3', 'BTC'), ('4', 'LP'), ('5', 'EUE'), ('6', 'NUE'), ('7', 'IJ'), ('8', 'VAM'), ('9', 'NEWVAM')], default='1', max_length=20, null=True)),
                ('wimaterial', models.CharField(blank=True, choices=[('1', 'Carbon_Steel'), ('2', 'CRA_9Cr'), ('3', 'CRA_13Cr'), ('4', 'Inconel')], default='1', max_length=20, null=True)),
                ('wishoedepth', models.FloatField()),
                ('wifloatCollar', models.FloatField()),
                ('wihangerDepth', models.FloatField()),
                ('wicementTop', models.FloatField()),
                ('wicasingGrade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casingGrades', to='wicasings.wicasinggrademodel')),
                ('wicasingSize', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casingSizes', to='wicasings.wicasingsizemodel')),
                ('wicasingWeight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casingWeights', to='wicasings.wicasingweightmodel')),
            ],
        ),
        migrations.AddField(
            model_name='wicasinggrademodel',
            name='wicasingWeight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wicasings.wicasingweightmodel'),
        ),
    ]
