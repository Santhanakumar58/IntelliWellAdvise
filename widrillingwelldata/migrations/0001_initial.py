# Generated by Django 5.0.1 on 2024-02-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WIDrillingWellData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgId', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wisurvey_Date', models.DateField()),
                ('wirkb_to_WH', models.FloatField()),
                ('wirkb_to_GL', models.FloatField()),
                ('wigl_to_MSL', models.FloatField()),
                ('wirkb_to_MSL', models.FloatField()),
                ('wiwh_to_MSL', models.FloatField()),
                ('wilattitude', models.CharField(max_length=20)),
                ('wilongitude', models.CharField(max_length=20)),
                ('witotal_Measured_Depth', models.FloatField()),
                ('witotal_True_Vertical_Depth', models.FloatField()),
                ('wiafe_No', models.CharField(max_length=40)),
            ],
        ),
    ]
