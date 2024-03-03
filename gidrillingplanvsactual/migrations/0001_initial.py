# Generated by Django 5.0.1 on 2024-02-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GIDrillingPlanVsActual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifgId', models.PositiveIntegerField()),
                ('giwellid', models.PositiveIntegerField()),
                ('gisection', models.TextField(choices=[('26_inch', '26_inch'), ('23_inch', '23_inch'), ('20_inch', '20_inch'), ('17_1/2_inch', '17_1/2_inch'), ('16_inch', '16_inch'), ('12_1/4_inch', '12_1/4_inch'), ('8_1/2_inch', '8_1/2_inch'), ('6_1/8_inch', '6_1/8_inch'), ('4_1/2_inch', '4_1/2_inch'), ('Completion', 'Completion'), ('Logging', 'Logging'), ('Well_Test', 'Well_Test')], default='26_inch', max_length=100)),
                ('gisection_Depth_Plan', models.FloatField()),
                ('giplan_Days', models.FloatField()),
                ('gisection_Depth_Actual', models.FloatField()),
                ('giactual_Days', models.FloatField()),
                ('gireason_for_Deviation', models.TextField(max_length=2000)),
            ],
        ),
    ]